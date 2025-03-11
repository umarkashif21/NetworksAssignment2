import networkx as nx, numpy as np, matplotlib.pyplot as plt
from scipy.stats import poisson

def generate_er_network(n,p,runs=30):
    avg_degrees=[]
    clustering_coeffs=[]
    path_lengths=[]

    for run in range(runs):
        print(f"Sim {run+1}/{runs} for (n={n},p={p})")
        G=nx.erdos_renyi_graph(n,p)

        #computing avg degree
        degrees=[deg for _,deg in G.degree()]
        avg_degrees.append(np.mean(degrees))

        #computing clustering coefficient
        clustering_coeffs.append(nx.average_clustering(G))

        #compute average path length (empirical for small, approx for large)
        if n <= 5000 and nx.is_connected(G):
            avg_path = nx.average_shortest_path_length(G)  
        else:
            avg_path=np.log(n)/np.log(p*n) #approximation
        
        path_lengths.append(avg_path) 
    
    avg_degree = np.mean(avg_degrees)
    avg_clustering = np.mean(clustering_coeffs)
    avg_path_length = np.mean(path_lengths)  
    
    return avg_degree, avg_clustering, avg_path_length, degrees

configurations=[(1000,0.01),(5000,0.002),(10000,0.0005)]
results={}

for n,p in configurations:
    avg_k,avg_c,avg_l,degrees=generate_er_network(n,p)
    results[(n,p)]=(avg_k,avg_c,avg_l)
    
    plt.figure()
    degree_counts=np.bincount(degrees)
    k_values=np.arange(len(degree_counts))
    probabilities=degree_counts/np.sum(degree_counts)
    plt.step(k_values,probabilities,where="mid",label=f"n={n},p={p}",linewidth=2,alpha=0.7)
    
    lambda_k=p*(n-1)
    poisson_dist=poisson.pmf(k_values,lambda_k)
    plt.plot(k_values,poisson_dist,'ro-',markersize=4,label="Poisson Fit")

    plt.xlabel("Degree k"),plt.ylabel("P(k)")
    plt.title(f"Degree Dist. for G({n},{p})")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

for (n,p),(avg_k,avg_c,avg_l) in results.items():
    print(f"Config (n={n},p={p}):")
    print(f"  - Avg Deg: {avg_k:.2f} (Theory: {p*(n-1):.2f})")
    print(f"  - Clustering: {avg_c:.4f} (Theory: {p:.4f})")
    print(f"  - Path Len: {avg_l:.2f} (Theory: {np.log(n)/np.log(p*n):.2f})\n")
