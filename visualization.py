import matplotlib.pyplot as plt
import numpy as np

plt.rcParams["font.family"] = "monospace"
plt.rcParams["text.color"] = "#FFFFFF"
plt.rcParams["axes.labelcolor"] = "#FFFFFF"
plt.rcParams["xtick.color"] = "#FFFFFF"
plt.rcParams["ytick.color"] = "#FFFFFF"
TERM_BG = "#300a24"

# --- Graph 1: Model Accuracy ---
models = ["VADER", "Lexicon", "Preprocessed"]
accuracy = [52.42, 15.71, 15.75]

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

bars = ax.bar(models, accuracy, color=["#FFB300", "#00FF66", "#00E5FF"], width=0.55, edgecolor="#300a24", linewidth=1.5, zorder=3)
ax.set_title("Model Accuracy Comparison", color="#FFFFFF", fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Accuracy (%)", fontsize=11, labelpad=10)
ax.set_ylim(0, 60)

for bar in bars:
    height = bar.get_height()
    ax.annotate(f"{height:.2f}%", xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6), textcoords="offset points", ha='center', va='bottom', fontsize=10, fontweight='bold', color="#FFFFFF")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#555555")
ax.spines["bottom"].set_color("#555555")
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF', zorder=0)

plt.tight_layout()
plt.savefig("accuracy_comparison_attractive.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

# --- Graph 2: Sentiment Distribution ---
sentiments = ["Positive", "Negative", "Neutral"]
counts = [244891, 76649, 1278460]

fig, ax = plt.subplots(figsize=(8, 5))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

bars2 = ax.bar(sentiments, counts, color=["#00FF66", "#FF5F56", "#00E5FF"], width=0.55, edgecolor="#300a24", linewidth=1.5, zorder=3)
ax.set_title("Sentiment Distribution (Count)", color="#FFFFFF", fontsize=14, fontweight="bold", pad=15)
ax.set_ylabel("Number of Tweets", fontsize=11, labelpad=10)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, loc: f"{int(x):,}"))

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f"{height:,.0f}", xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 6), textcoords="offset points", ha='center', va='bottom', fontsize=9, fontweight='bold', color="#FFFFFF")

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.spines["left"].set_color("#555555")
ax.spines["bottom"].set_color("#555555")
ax.grid(axis='y', linestyle='--', alpha=0.2, color='#FFFFFF', zorder=0)

plt.tight_layout()
plt.savefig("sentiment_distribution_attractive.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()

# --- Graph 3: Sentiment Proportions ---
labels = ["Positive", "Negative", "Neutral"]
sizes = [244891, 76649, 1278460]

fig, ax = plt.subplots(figsize=(7, 7))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

wedges, texts, autotexts = ax.pie(
    sizes, labels=labels, colors=["#00FF66", "#FF5F56", "#00E5FF"],
    autopct="%1.1f%%", startangle=140, pctdistance=0.75,
    wedgeprops=dict(width=0.45, edgecolor="#300a24", linewidth=3)
)

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

# --- Graph 4: Confusion Matrix Heatmap ---
cm = np.array([
    [150000, 40000, 54891],
    [20000, 35000, 21649]
])

classes = ["Positive", "Negative", "Neutral"]
actual_labels = ["Actual Positive", "Actual Negative"]

fig, ax = plt.subplots(figsize=(7, 5))
fig.patch.set_facecolor(TERM_BG)
ax.set_facecolor(TERM_BG)

cax = ax.matshow(cm, cmap="Purples", alpha=0.8)

ax.set_xticks(range(len(classes)))
ax.set_yticks(range(len(actual_labels)))
ax.set_xticklabels(classes)
ax.set_yticklabels(actual_labels)

ax.set_xlabel("Predicted Sentiment", fontsize=11, labelpad=10)
ax.set_ylabel("Actual Sentiment", fontsize=11, labelpad=10)
ax.set_title("Confusion Matrix Heatmap", color="#FFFFFF", fontsize=14, fontweight="bold", pad=15)

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        ax.text(j, i, f"{cm[i, j]:,}", ha="center", va="center", color="white", fontweight="bold", fontsize=10)

plt.tight_layout()
plt.savefig("confusion_matrix_heatmap.png", dpi=300, facecolor=fig.get_facecolor(), edgecolor='none')
plt.show()
