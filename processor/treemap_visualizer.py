# processor/treemap_visualizer.py

import squarify
import matplotlib.pyplot as plt

def draw_treemap(keywords, title="주요 키워드 트리맵"):
    """
    키워드 리스트를 받아 트리맵 시각화
    입력: [('금리', 24), ('미국', 19), ...]
    """
    labels = [f"{word}\n{count}" for word, count in keywords]
    sizes = [count for _, count in keywords]
    colors = plt.cm.Oranges([0.4 + 0.6 * (i / len(sizes)) for i in range(len(sizes))])

    plt.figure(figsize=(12, 8))
    squarify.plot(sizes=sizes, label=labels, color=colors, alpha=0.9)
    plt.axis('off')
    plt.title(title, fontsize=20)
    plt.tight_layout()
    plt.show()