import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

presets = {
    "Smooth": (0.20, 0.50, 0.25),
    "Balanced": (0.20, 0.60, 0.35),
    "Strong Growth": (0.15, 0.80, 0.20),
    "Strong Decay": (0.25, 0.55, 0.55),
    "Dramatic Change": (0.10, 0.85, 0.60),
    "Custom (Manual Input)": None
}

def apply_preset(event):
    selected = preset_box.get()
    if presets[selected] is not None:
        p0_val, p_close_val, p_decay_val = presets[selected]

        entry_p0.delete(0, tk.END)
        entry_pclose.delete(0, tk.END)
        entry_pdecay.delete(0, tk.END)

        entry_p0.insert(0, str(p0_val))
        entry_pclose.insert(0, str(p_close_val))
        entry_pdecay.insert(0, str(p_decay_val))

def suggest_values(*args):
    try:
        N = int(entry_nodes.get())
    except:
        return
    
    if N <= 15:
        p0_val, p_close_val, p_decay_val = (0.20, 0.65, 0.35)
    elif N <= 100:
        p0_val, p_close_val, p_decay_val = (0.10, 0.45, 0.30)
    else:
        p0_val, p_close_val, p_decay_val = (0.03, 0.25, 0.20)

    entry_p0.delete(0, tk.END)
    entry_p0.insert(0, str(p0_val))

    entry_pclose.delete(0, tk.END)
    entry_pclose.insert(0, str(p_close_val))

    entry_pdecay.delete(0, tk.END)
    entry_pdecay.insert(0, str(p_decay_val))

def start_simulation():
    try:
        N = int(entry_nodes.get())
        p0 = float(entry_p0.get())
        p_close = float(entry_pclose.get())
        p_decay = float(entry_pdecay.get())
        steps = int(entry_steps.get())
        snapshot_every = int(entry_snapshot.get())

        if not(0 <= p0 <= 1 and 0 <= p_close <= 1 and 0 <= p_decay <= 1):
            messagebox.showerror("Error", "Probabilities must be between 0 and 1.")
            return
        
        if p0 + p_close > 1:
            messagebox.showerror("Error", "p0 + p_close cannot exceed 1.")
            return
        
        root.destroy()
        run_simulation(N, p0, p_close, p_decay, steps, snapshot_every)

    except ValueError:
        messagebox.showerror("Error", "Enter numeric values only!")

def approx_avg_shortest_path_length(G, samples=200):
    if len(G) == 0:
        return 0.0
    if nx.is_connected(G):
        comp_nodes = list(G.nodes())
    else:
        comp_nodes = list(max(nx.connected_components(G), key=len))
    if len(comp_nodes) < 2:
        return 0.0

    total = 0
    count = 0
    samples = min(samples, len(comp_nodes)*(len(comp_nodes)-1)//2)

    for _ in range(samples):
        u, v = random.sample(comp_nodes, 2)
        try:
            total += nx.shortest_path_length(G, u, v)
            count += 1
        except:
            pass
    return total/count if count > 0 else float("inf")


def record_metrics(G, t, sample_pairs_for_L):
    return {
        "time": t,
        "num_edges": G.number_of_edges(),
        "avg_degree": sum(dict(G.degree()).values()) / len(G),
        "transitivity": nx.transitivity(G),
        "avg_clustering": nx.average_clustering(G),
        "avg_shortest_path": approx_avg_shortest_path_length(G, sample_pairs_for_L),
    }

def growth_phase(G, p_close):
    open_pairs = set()
    for w in G.nodes():
        nbrs = list(G.neighbors(w))
        if len(nbrs) < 2:
            continue
        for i in range(len(nbrs)):
            for j in range(i+1, len(nbrs)):
                u, v = nbrs[i], nbrs[j]
                if not G.has_edge(u, v):
                    open_pairs.add(tuple(sorted((u, v))))

    for u, v in open_pairs:
        if random.random() <= p_close:
            G.add_edge(u, v)


def decay_phase(G, p_decay):
    for e in list(G.edges()):
        if random.random() <= p_decay:
            G.remove_edge(*e)

def run_simulation(N, p0, p_close, p_decay, steps, snapshot_every):

    G = nx.erdos_renyi_graph(N, p0)

    metrics = []
    snapshots = []
    half = steps // 2

    metrics.append(record_metrics(G, 0, 200))
    snapshots.append((0, G.copy()))

    for t in range(1, steps+1):
        if t <= half:
            growth_phase(G, p_close)
        else:
            decay_phase(G, p_decay)

        metrics.append(record_metrics(G, t, 200))

        if not(t % snapshot_every):
            snapshots.append((t, G.copy()))


    times = [m["time"] for m in metrics]
    edges = [m["num_edges"] for m in metrics]
    deg = [m["avg_degree"] for m in metrics]
    trans = [m["transitivity"] for m in metrics]
    clust = [m["avg_clustering"] for m in metrics]
    spl = [m["avg_shortest_path"] for m in metrics]

    plt.figure(figsize=(12, 8))
    plt.subplot(2, 2, 1); plt.plot(times, edges, "-o"); plt.title("Edges over time")
    plt.subplot(2, 2, 2); plt.plot(times, deg, "-o"); plt.title("Degree over time")
    plt.subplot(2, 2, 3); plt.plot(times, clust, "-o", label="Clustering")
    plt.plot(times, trans, "-s", label="Transitivity"); plt.legend()
    plt.subplot(2, 2, 4); plt.plot(times, spl, "-o"); plt.title("Shortest Path over time")
    plt.tight_layout(); plt.show()

    
    fig, ax = plt.subplots(figsize=(6, 6))
    pos = nx.spring_layout(snapshots[0][1], seed=42)
    ax.axis("off")

    def draw(frame):
        ax.clear(); ax.axis("off")
        t_s, G_s = snapshots[frame]
        pos_u = nx.spring_layout(G_s, pos=pos, iterations=8)
        for k in pos: pos[k] = pos_u[k]
        nx.draw_networkx_nodes(G_s, pos, node_color="skyblue", node_size=100, ax=ax)
        nx.draw_networkx_edges(G_s, pos, alpha=0.6, ax=ax)
        ax.set_title(f"t = {t_s}")

    ani = animation.FuncAnimation(fig,draw,frames=len(snapshots), interval=500, repeat=False)

    try:
        ani.save("network_evolution.mp4", dpi=150, writer="ffmpeg")
    except:
        ani.save("network_evolution.gif", dpi=150, writer="pillow")

    plt.show()


root = tk.Tk()
root.title("Triadic Closure Simulation")
root.geometry("430x520")
root.config(bg="#1e1e2f")

tk.Label(root, text="Triadic Closure Simulation", bg="#1e1e2f", fg="white",
         font=("Helvetica", 16, "bold")).pack(pady=10)


tk.Label(root, text="Presets:", bg="#1e1e2f", fg="white").pack()
preset_box = ttk.Combobox(root, values=list(presets.keys()), state="readonly", width=25)
preset_box.pack(pady=4)
preset_box.current(1)
preset_box.bind("<<ComboboxSelected>>", apply_preset)

frame = tk.Frame(root, bg="#1e1e2f")
frame.pack()

fields = [
    "Friends (nodes):", "Initial Probability (p₀):", 
    "Closure Probability (p_close):", "Decay Probability (p_decay):", 
    "Time Steps (T):", "Snapshot Interval:"
]

entries = []
for f in fields:
    tk.Label(frame, text=f, bg="#1e1e2f", fg="white").pack(pady=2)
    e = tk.Entry(frame, justify="center")
    e.pack()
    entries.append(e)

entry_nodes, entry_p0, entry_pclose, entry_pdecay, entry_steps, entry_snapshot = entries

# Defaults
entry_nodes.insert(0, "10")
entry_steps.insert(0, "10")
entry_snapshot.insert(0, "1")

entry_nodes.bind("<KeyRelease>", suggest_values)

tk.Button(root, text="Run Simulation", bg="#4CAF50", fg="white",
          font=("Helvetica", 12, "bold"), command=start_simulation).pack(pady=10)

root.mainloop()
