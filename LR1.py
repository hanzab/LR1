import streamlit as st
from PIL import Image
from collections import deque

img_path = "image1.jpg"
image = Image.open(img_path)
st.image(image, caption="Image from LR1", use_column_width=True)

# Define the directed graph
graph = {
    'A': ['B', 'D'],
    'B': ['C', 'E', 'G'],
    'C': ['A'],
    'D': ['C'],
    'E': ['H'],
    'F': [],
    'G': ['H'],
    'H': ['F', 'G']
}

# Sort adjacency lists alphabetically
for node in graph:
    graph[node].sort()

# BFS function
def bfs(start):
    visited = []
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

# DFS function
def dfs(start, visited=None):
    if visited is None:
        visited = []
    visited.append(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(neighbor, visited)
    return visited

# --- Streamlit Interface ---
st.title("📊 Graph Traversal Summary")

start_node = st.selectbox("Select the starting node:", list(graph.keys()))

if st.button("Run Traversals"):
    bfs_order = bfs(start_node)
    dfs_order = dfs(start_node)
    
    # Display styled summary
    st.markdown("### 🔹 Traversal Results")
    
    st.markdown(f"*Start Node:* {start_node}")
    
    st.markdown(f"*Breadth-First Search (BFS) Order:*\n\n➡  {' → '.join(bfs_order)}")
    st.markdown(f"*Depth-First Search (DFS) Order:*\n\n➡  {' → '.join(dfs_order)}")
    
    # Optional: display visited nodes as bullet points
    st.markdown("*BFS Path:*")
    for node in bfs_order:
        st.markdown(f"- {node}")
    
    st.markdown("*DFS Path:*")
    for node in dfs_order:
        st.markdown(f"- {node}")