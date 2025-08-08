def convert_hku_to_slf_correct(hku_file, slf_file):
    """Convert HKU format to match SLF's expected format exactly"""
    
    vertices = {}
    edges = []
    
    with open(hku_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
                
            if parts[0] == 't':  
                continue
            elif parts[0] == 'v':  # v id label degree
                vertex_id = int(parts[1])
                label = int(parts[2])
                vertices[vertex_id] = label
            elif parts[0] == 'e':  # e src dst label  
                src = int(parts[1])
                dst = int(parts[2])
                edges.append((src, dst))
    
    # Write in exact SLF format
    with open(slf_file, 'w') as f:
        f.write(f"{len(vertices)}\n")
        for vid in sorted(vertices.keys()):
            f.write(f"{vid} {vertices[vid]}\n")

# Try smaller query first
print("Converting small query...")
convert_hku_to_slf_correct('/Users/williampark/desktop/dataset/dblp/query_graph/query_dense_8_1.graph', 'small_query.grf')

# Create smaller target sample
with open('small_target.grf', 'w') as f:
    f.write("100\n")
    for i in range(100):
        f.write(f"{i} {i%10}\n")

print("Created small test files")
