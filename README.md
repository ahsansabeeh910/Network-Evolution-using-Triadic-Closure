<div align="center">

# 🌐 Network Evolution using Triadic Closure

### Social Network Analysis & Dynamic Graph Evolution Simulator

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![NetworkX](https://img.shields.io/badge/NetworkX-Graph%20Analysis-green?style=for-the-badge)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-red?style=for-the-badge)
![Social Network Analysis](https://img.shields.io/badge/SNA-Network%20Science-purple?style=for-the-badge)

</div>

---

# 📌 Overview

This project presents a **Social Network Analysis (SNA)** simulation platform that models how networks evolve over time using the principle of **Triadic Closure**.

The system begins with a random Erdős–Rényi graph and progressively forms new connections between nodes that share mutual neighbors, simulating real-world friendship formation and community development. :contentReference[oaicite:1]{index=1}

The project demonstrates how simple local interaction rules can generate:

✅ Dense Clusters  
✅ Community Structures  
✅ Social Connectivity Growth  
✅ Dynamic Network Evolution  

The simulation also supports optional edge decay to mimic weakening relationships over time.

---

# 🚀 Features

✅ Interactive Tkinter GUI  
✅ Erdős–Rényi Random Graph Generation  
✅ Automated Triadic Closure Simulation  
✅ Edge Decay Modeling  
✅ Dynamic Network Evolution  
✅ Real-time Graph Metrics Calculation  
✅ Animated Network Visualization  
✅ Time-Series Plot Generation  
✅ Snapshot-based Graph Evolution  

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Core programming language |
| NetworkX | Graph creation & analysis |
| Tkinter | GUI development |
| Matplotlib | Graph plotting & animation |
| NumPy | Numerical computation |
| Random Module | Probabilistic edge generation |

---

# 🧠 Triadic Closure Concept

Triadic closure is a common phenomenon in social networks:

```text
If A is connected to B
and B is connected to C
then A is more likely to connect with C
```

This process gradually transforms sparse networks into highly clustered social communities.

---

# ⚙️ Workflow

The simulation follows these stages:

1️⃣ User inputs simulation parameters  
2️⃣ Random graph generation  
3️⃣ Open triad detection  
4️⃣ Edge formation using closure probability  
5️⃣ Optional edge decay  
6️⃣ Metric computation  
7️⃣ Graph visualization & animation  

The workflow diagram included in the report visually illustrates the complete simulation pipeline. :contentReference[oaicite:2]{index=2}

---

# 📊 Network Metrics Analyzed

The system continuously computes:

| Metric | Description |
|--------|-------------|
| Average Degree | Overall network connectivity |
| Transitivity | Triangle density in graph |
| Clustering Coefficient | Community formation measure |
| Shortest Path Length | Network accessibility |

These metrics help analyze how social structures evolve over time. :contentReference[oaicite:3]{index=3}

---

# 🖥️ GUI Features

The Tkinter interface allows users to configure:

- Number of nodes
- Initial edge probability (p₀)
- Closure probability (p_close)
- Decay probability (p_decay)
- Time steps
- Snapshot interval

The GUI screenshots are shown in the project report output section. :contentReference[oaicite:4]{index=4}

---

# 📂 Project Structure

```bash
Network-Evolution-Triadic-Closure/
│
├── app.py
├── outputs/
├── animations/
├── screenshots/
├── report/
└── README.md
```

---

# 📥 Installation

## Clone Repository

```bash
git clone https://github.com/ahsansabeeh910/Network-Evolution-Triadic-Closure.git
```

## Navigate to Project

```bash
cd Network-Evolution-Triadic-Closure
```

## Install Dependencies

```bash
pip install networkx matplotlib numpy
```

---

# ▶️ Run Project

```bash
python app.py
```

---

# 📈 Simulation Process

## 🔹 Growth Phase

- Detects open triads
- Forms new edges probabilistically
- Increases clustering & connectivity

## 🔹 Decay Phase

- Randomly removes edges
- Simulates weakening relationships
- Maintains dynamic restructuring

---

# 🎞️ Visualization Output

The project generates:

✅ Time-series metric plots  
✅ Animated graph evolution  
✅ Dynamic clustering visualization  
✅ Edge formation progression  

Animations are exported as:

- MP4 (FFmpeg)
- GIF (Pillow fallback)

---

# 📊 Key Observations

The simulation demonstrates:

- Sparse graphs gradually become clustered
- Average degree increases over time
- Transitivity improves significantly
- Shortest path distances decrease
- Communities emerge naturally

The plotted graphs and network snapshots in the report visually validate these trends. :contentReference[oaicite:5]{index=5}

---

# 📚 Real-World Applications

- Social Media Analysis
- Recommendation Systems
- Community Detection
- Epidemiology Modeling
- Information Diffusion
- Online Friendship Networks
- Behavioral Network Research

---

# 🔮 Future Improvements

- Real-world social network datasets
- Directed & weighted graphs
- Community-aware node behavior
- Machine Learning based link prediction
- Large-scale parallel simulations
- Real-time dashboard visualization

The report also discusses future enhancements for scalability and realistic modeling. :contentReference[oaicite:6]{index=6}

---

# 📚 References

1. NetworkX Documentation  
2. Matplotlib Documentation  
3. Python Official Documentation  
4. Barabási – *Network Science*  
5. GeeksforGeeks – Triadic Closure in Social Networks  

:contentReference[oaicite:7]{index=7}

---

# 👨‍💻 Authors

### Sabeeh Ahsan  

**Jaypee Institute of Information Technology**

---
