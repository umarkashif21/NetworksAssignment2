# NetworksAssignment2

# Erdős-Rényi Network Analysis  

This repository contains the implementation and analysis of Erdős-Rényi (E-R) random graphs for different configurations of \( n \) (number of nodes) and \( p \) (probability of edge formation).  

##  Problem Statement  

We generate an E-R network \( G(n, p) \) for three different configurations and compute the following network properties:  

1. **Average Degree**  
2. **Average Clustering Coefficient**  
3. **Average Path Length**  
4. **Degree Distribution (with Poisson Fit)**  

Each configuration is simulated **30 times**, and the average values are reported and compared with theoretical predictions.

## Implementation  

- The program uses **NetworkX** for graph generation and analysis.  
- The results include calculated values and degree distribution plots for each configuration.   

## Results  

| Configuration (n, p) | Avg Degree (Simulated) | Avg Degree (Theory) | Clustering (Simulated) | Clustering (Theory) | Path Length (Simulated) | Path Length (Theory) |
|----------------------|------------------------|----------------------|------------------------|----------------------|-------------------------|-----------------------|
| (1000, 0.01)        | 10.01                   | 9.99                 | 0.0099                 | 0.0100               | 3.25                    | 3.00                  |
| (5000, 0.002)       | 10.00                   | 10.00                | 0.0020                 | 0.0020               | 3.87                    | 3.70                  |
| (10000, 0.0005)     | 5.01                    | 5.00                 | 0.0005                 | 0.0005               | 5.72                    | 5.72                  |


