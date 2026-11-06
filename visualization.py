import matplotlib.pyplot as plt

# -----------------------
# Ubuntu Terminal Styling Setup
# -----------------------
plt.rcParams["font.family"] = "monospace"
plt.rcParams["text.color"] = "#FFFFFF"
plt.rcParams["axes.labelcolor"] = "#FFFFFF"
plt.rcParams["xtick.color"] = "#FFFFFF"
plt.rcParams["ytick.color"] = "#FFFFFF"

# Ubuntu terminal background color (deep aubergine/purple)
TERM_BG = "#300a24"

# -----------------------
# Graph 1: Accuracy Comparison
# -----------------------
models = ["VADER", "Lexicon", "Preprocessed"]
accuracy = [52.42, 15.71, 15.75]

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

# Vibrant, glowing terminal accent colors
bar_colors = ["#FFB300", "#00FF66", "#00E5FF"]
bars = ax.bar(models, accuracy, color=bar_colors, width=0.55, edgecolor="#300a24", linewidth=1.5, zorder=3)

ax.set_title("Model Accuracy Comparison", color="#FFFFFF", fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Accuracy (%)", fontsize=11, labelpad=10)
ax.set_ylim(0, 60)

# Add exact value labels on top of each bar
for bar in bars:
    height = bar.get_height()
    ax.annotate(f"{height:.2f}%",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),  # 6 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom', fontsize=10, fontweight='bold', color="#FFFFFF")

# Clean spines and add subtle gridlines
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#555555")
ax.spines["bottom"].set_color("#555555")
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF', zorder=0)

plt.tight_layout()
plt.savefig("accuracy_comparison_attractive.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

# -----------------------
# Graph 2: Sentiment Distribution (Bar Chart)
# -----------------------
sentiments = ["Positive", "Negative", "Neutral"]
counts = [244891, 76649, 1278460]

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

bar_colors_sent = ["#00FF66", "#FF5F56", "#00E5FF"]
bars2 = ax.bar(sentiments, counts, color=bar_colors_sent, width=0.55, edgecolor="#300a24", linewidth=1.5, zorder=3)

ax.set_title("Sentiment Distribution (Count)", color="#FFFFFF", fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Number of Tweets", fontsize=11, labelpad=10)

# Format y-axis labels cleanly in millions/thousands
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x):,}"))

# Add exact count labels on top of bars
for bar in bars2:
    height = bar.get_height()
    ax.annotate(f"{height:,.0f}",
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6),
                textcoords="offset points",
                ha='center', va='bottom', fontsize=9, fontweight='bold', color="#FFFFFF")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#555555")
ax.spines["bottom"].set_color("#555555")
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF', zorder=0)

plt.tight_layout()
plt.savefig("sentiment_distribution_attractive.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

# -----------------------
# Graph 3: Sentiment Distribution (Pie Chart)
# -----------------------
labels = ["Positive", "Negative", "Neutral"]
sizes = [244891, 76649, 1278460]

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

pie_colors = ["#00FF66", "#FF5F56", "#00E5FF"]
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    colors=pie_colors,
    autopct="%1.1f%%",
    startangle=140,
    pctdistance=0.75,
    wedgeprops=dict(width=0.45, edgecolor="#300a24", linewidth=3) # Turned into a modern Donut Chart!
)

# Styling text inside the donut chart
for text in texts:
    text.set_color("#FFFFFF")
    text.set_fontsize(11)
for autotext in autotexts:
    autotext.set_color("#FFFFFF")
    autotext.set_weight("bold")
    autotext.set_fontsize(10)

ax.set_title("Sentiment Proportions", color="#FFFFFF", fontsize=14, fontweight="bold", pad=20)

plt.tight_layout()
plt.savefig("sentiment_donut_chart_attractive.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()