def convert_hku_to_slf(hku_file, slf_file):
    """Convert HKU .graph format to SLF .grf format"""
    
    vertices = {}
    edges = []
    
    with open(hku_file, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if not parts:
                continue
                
            if parts[0] == 't':  # pattern header: t vertex_count edge_count
                continue  # skip header
            elif parts[0] == 'v':  # vertex: v id label degree
                vertex_id = int(parts[1])
                label = int(parts[2])
                vertices[vertex_id] = label
            elif parts[0] == 'e':  # edge: e src dst label
                src = int(parts[1])
                dst = int(parts[2])
                edges.append((src, dst))
    
    # Write SLF format: vertex_count, then vertices with labels, then edges
    with open(slf_file, 'w') as f:
        f.write(f"{len(vertices)}\n")
        for vid in sorted(vertices.keys()):
            f.write(f"{vid} {vertices[vid]}\n")
        for src, dst in edges:
            f.write(f"{src} {dst}\n")

# Convert target graph
print("Converting target graph...")
convert_hku_to_slf('/Users/williampark/desktop/dataset/dblp/data_graph/dblp.graph', 'dblp_target.grf')

# Convert query graphs
print("Converting query graphs...")
convert_hku_to_slf('/Users/williampark/desktop/dataset/dblp/query_graph/query_dense_8_186.graph', 'query_8v.grf')
convert_hku_to_slf('/Users/williampark/desktop/dataset/dblp/query_graph/query_dense_24_50.graph', 'query_24v.grf')
convert_hku_to_slf('/Users/williampark/desktop/dataset/dblp/query_graph/query_dense_32_140.graph', 'query_32v.grf')

print("Conversion complete!")
