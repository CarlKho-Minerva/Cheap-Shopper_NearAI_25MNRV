import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import psutil
import time

# Set the visual style for the plots
sns.set(style="whitegrid")
plt.rcParams['figure.figsize'] = (12, 8)

# Raw benchmark data
raw_data = {
    'participant': ['Minjae', 'Minjae', 'Minjae', 'Minjae', 'Minjae',
                    'Jeevan', 'Jeevan', 'Jeevan', 'Jeevan', 'Jeevan',
                    'Uliana', 'Uliana', 'Uliana', 'Uliana', 'Uliana'],
    'query': ['Find cheap laptops', 'Best budget smartphones', 'Affordable headphones', 'Discount gaming mice', 'Budget keyboards',
              'Cheap monitors', 'Budget tablets', 'Affordable smart watches', 'Discount webcams', 'Budget speakers',
              'Find cheap SSDs', 'Budget RAM', 'Affordable GPUs', 'Discount CPUs', 'Budget motherboards'],
    'query_understood': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'link_generated': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    'feature_relevance_score': [0.85, 0.78, 0.82, 0.75, 0.82, 0.77, 0.83, 0.79, 0.82, 0.80, 0.75, 0.85, 0.78, 0.80, 0.82],
    'response_time_seconds': [5.2, 4.8, 6.1, 5.5, 4.9, 6.3, 5.8, 6.2, 5.7, 6.0, 5.5, 6.2, 6.4, 5.9, 5.3],
    'task_completed': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    # Adding error metrics
    'semantic_errors': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'technical_errors': [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0],
    # Resource utilization (mock data)
    'memory_usage_mb': [120, 125, 122, 128, 121, 130, 127, 124, 126, 129, 123, 125, 128, 126, 122],
    'cpu_utilization': [25, 28, 30, 27, 26, 29, 31, 28, 27, 30, 26, 29, 32, 28, 27]
}

# Baseline comparison data
baseline_data = {
    'system': ['Cheap-Shopper', 'Baseline A', 'Baseline B'],
    'query_understanding': [100, 85, 92],
    'link_generation': [100, 80, 95],
    'feature_relevance': [80, 70, 75],
    'avg_response_time': [5.7, 3.2, 8.5],
    'task_completion': [100, 85, 90],
    'error_rate': [2, 8, 5],
    'memory_usage': [125, 180, 220],
    'cpu_utilization': [28, 35, 45]
}

# Success criteria definitions
success_criteria = {
    'Query Understanding': {'target': 95, 'stretch': 100, 'status': 'Achieved'},
    'Link Generation': {'target': 95, 'stretch': 100, 'status': 'Achieved'},
    'Feature Relevance': {'target': 85, 'stretch': 95, 'status': 'Below Target'},
    'Response Time': {'target': 3.0, 'stretch': 2.0, 'status': 'Below Target'},
    'Task Completion': {'target': 95, 'stretch': 100, 'status': 'Achieved'},
    'Error Rate': {'target': 5, 'stretch': 2, 'status': 'Achieved'},
    'Memory Usage': {'target': 150, 'stretch': 100, 'status': 'Achieved'},
    'CPU Utilization': {'target': 35, 'stretch': 25, 'status': 'On Target'}
}

# Convert to DataFrame
df = pd.DataFrame(raw_data)
baseline_df = pd.DataFrame(baseline_data)

# Calculate aggregated metrics
metrics = {
    'Query Understanding': df['query_understood'].mean() * 100,
    'Link Generation': df['link_generated'].mean() * 100,
    'Feature Relevance': df['feature_relevance_score'].mean() * 100,
    'Avg Response Time (s)': df['response_time_seconds'].mean(),
    'Task Completion': df['task_completed'].mean() * 100
}

print("Overall Metrics:")
for metric, value in metrics.items():
    print(f"{metric}: {value:.2f}")

# Calculate error metrics
error_metrics = {
    'Semantic Errors': df['semantic_errors'].sum(),
    'Technical Errors': df['technical_errors'].sum(),
    'Total Errors': df['semantic_errors'].sum() + df['technical_errors'].sum(),
    'Error Rate (%)': (df['semantic_errors'].sum() + df['technical_errors'].sum()) / len(df) * 100
}

# Resource utilization metrics
resource_metrics = {
    'Average Memory Usage (MB)': df['memory_usage_mb'].mean(),
    'Peak Memory Usage (MB)': df['memory_usage_mb'].max(),
    'Average CPU Utilization (%)': df['cpu_utilization'].mean(),
    'Peak CPU Utilization (%)': df['cpu_utilization'].max()
}

print("\nError Metrics:")
for metric, value in error_metrics.items():
    print(f"{metric}: {value:.2f}")

print("\nResource Utilization Metrics:")
for metric, value in resource_metrics.items():
    print(f"{metric}: {value:.2f}")

# Calculate metrics by participant
participant_metrics = df.groupby('participant').agg({
    'query_understood': 'mean',
    'link_generated': 'mean',
    'feature_relevance_score': 'mean',
    'response_time_seconds': 'mean',
    'task_completed': 'mean'
}).reset_index()

# Convert to percentages for visualization
participant_metrics['query_understood'] *= 100
participant_metrics['link_generated'] *= 100
participant_metrics['feature_relevance_score'] *= 100
participant_metrics['task_completed'] *= 100

# Create visualizations
def create_bar_chart():
    """Create a bar chart for key performance metrics"""
    metrics_df = pd.DataFrame({
        'Metric': ['Query Understanding', 'Link Generation', 'Feature Relevance', 'Task Completion'],
        'Value': [metrics['Query Understanding'], metrics['Link Generation'],
                  metrics['Feature Relevance'], metrics['Task Completion']]
    })

    plt.figure(figsize=(10, 6))
    colors = ['#3498db', '#3498db', '#e74c3c', '#3498db']  # Highlight feature relevance as different
    ax = sns.barplot(x='Metric', y='Value', data=metrics_df, palette=colors)

    plt.title('Key Performance Metrics', fontsize=16)
    plt.ylabel('Percentage (%)', fontsize=12)
    plt.xlabel('Metric', fontsize=12)
    plt.ylim(0, 105)  # To show the full 100% with some margin

    # Add text annotations on bars
    for i, row in enumerate(metrics_df.itertuples()):
        ax.text(i, row.Value + 2, f"{row.Value:.1f}%", ha='center', fontsize=12)

    # Save the figure
    plt.tight_layout()
    plt.savefig('key_metrics.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_response_time_chart():
    """Create a chart for response time by participant"""
    plt.figure(figsize=(10, 6))
    sns.barplot(x='participant', y='response_time_seconds', data=df)
    plt.axhline(y=3.0, color='green', linestyle='--', alpha=0.7, label='Target threshold')
    plt.title('Average Response Time by Participant', fontsize=16)
    plt.ylabel('Response Time (seconds)', fontsize=12)
    plt.xlabel('Participant', fontsize=12)
    plt.ylim(0, max(df['response_time_seconds']) * 1.2)
    plt.legend()

    # Save the figure
    plt.tight_layout()
    plt.savefig('response_time.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_radar_chart():
    """Create a radar chart comparing participants across metrics"""
    # Prepare data for radar chart
    metrics_names = ['Query\nUnderstanding', 'Link\nGeneration',
                     'Feature\nRelevance', 'Task\nCompletion']

    # Number of variables
    N = len(metrics_names)

    # Create angles for each metric
    angles = [n / float(N) * 2 * np.pi for n in range(N)]
    angles += angles[:1]  # Close the polygon

    # Create figure
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))

    # Add lines for each participant
    for idx, participant in enumerate(participant_metrics['participant'].unique()):
        values = participant_metrics[participant_metrics['participant'] == participant]
        stats = [values['query_understood'].iloc[0],
                 values['link_generated'].iloc[0],
                 values['feature_relevance_score'].iloc[0],
                 values['task_completed'].iloc[0]]
        stats += stats[:1]  # Close the polygon

        ax.plot(angles, stats, linewidth=2, label=participant)
        ax.fill(angles, stats, alpha=0.1)

    # Set ticks and labels
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(metrics_names)
    ax.set_yticklabels([])

    # Add y-axis grid lines
    ax.set_yticks([25, 50, 75, 100])
    ax.set_yticklabels(['25%', '50%', '75%', '100%'])
    ax.set_ylim(0, 100)

    # Add title and legend
    plt.title('Metrics by Participant', size=15)
    plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    # Save the figure
    plt.tight_layout()
    plt.savefig('participant_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_baseline_comparison():
    """Create a comparison chart against baseline systems"""
    metrics_to_compare = ['query_understanding', 'link_generation', 'feature_relevance',
                         'task_completion', 'error_rate']

    plt.figure(figsize=(12, 8))

    # Set width of bars
    barWidth = 0.2

    # Set positions of the bars on X axis
    r1 = np.arange(len(metrics_to_compare))
    r2 = [x + barWidth for x in r1]
    r3 = [x + barWidth for x in r2]

    # Create bars
    plt.bar(r1, baseline_df[metrics_to_compare].iloc[0], width=barWidth, label=baseline_df['system'][0], color='#3498db')
    plt.bar(r2, baseline_df[metrics_to_compare].iloc[1], width=barWidth, label=baseline_df['system'][1], color='#e74c3c')
    plt.bar(r3, baseline_df[metrics_to_compare].iloc[2], width=barWidth, label=baseline_df['system'][2], color='#2ecc71')

    # Add labels and title
    plt.xlabel('Metrics', fontsize=12)
    plt.ylabel('Percentage / Rate', fontsize=12)
    plt.title('System Comparison Against Baselines', fontsize=16)
    plt.xticks([r + barWidth for r in range(len(metrics_to_compare))],
              ['Query\nUnderstanding', 'Link\nGeneration', 'Feature\nRelevance',
               'Task\nCompletion', 'Error\nRate'])
    plt.legend()

    # Save the figure
    plt.tight_layout()
    plt.savefig('baseline_comparison.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_error_analysis():
    """Create visualization for error analysis"""
    error_by_participant = df.groupby('participant').agg({
        'semantic_errors': 'sum',
        'technical_errors': 'sum'
    }).reset_index()

    error_by_participant['total_errors'] = error_by_participant['semantic_errors'] + error_by_participant['technical_errors']

    plt.figure(figsize=(10, 6))

    x = np.arange(len(error_by_participant['participant']))
    width = 0.35

    plt.bar(x - width/2, error_by_participant['semantic_errors'], width, label='Semantic Errors')
    plt.bar(x + width/2, error_by_participant['technical_errors'], width, label='Technical Errors')

    plt.xlabel('Participant')
    plt.ylabel('Number of Errors')
    plt.title('Error Analysis by Participant')
    plt.xticks(x, error_by_participant['participant'])
    plt.legend()

    plt.tight_layout()
    plt.savefig('error_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_resource_utilization():
    """Create visualization for resource utilization"""
    plt.figure(figsize=(12, 6))

    # Create subplot for the 2 metrics
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

    # Memory usage by participant
    sns.barplot(x='participant', y='memory_usage_mb', data=df, ax=ax1)
    ax1.set_title('Memory Usage by Participant')
    ax1.set_ylabel('Memory Usage (MB)')
    ax1.set_xlabel('Participant')

    # CPU utilization by participant
    sns.barplot(x='participant', y='cpu_utilization', data=df, ax=ax2)
    ax2.set_title('CPU Utilization by Participant')
    ax2.set_ylabel('CPU Utilization (%)')
    ax2.set_xlabel('Participant')

    plt.tight_layout()
    plt.savefig('resource_utilization.png', dpi=300, bbox_inches='tight')
    plt.close()

def create_success_criteria_chart():
    """Create a chart showing performance against success criteria"""
    metrics = list(success_criteria.keys())
    current_values = [
        metrics['Query Understanding'],
        metrics['Link Generation'],
        metrics['Feature Relevance'],
        metrics['Avg Response Time (s)'],
        metrics['Task Completion'],
        error_metrics['Error Rate (%)'],
        resource_metrics['Average Memory Usage (MB)'],
        resource_metrics['Average CPU Utilization (%)']
    ]
    targets = [success_criteria[m]['target'] for m in metrics]
    stretch = [success_criteria[m]['stretch'] for m in metrics]

    plt.figure(figsize=(12, 8))
    x = np.arange(len(metrics))
    width = 0.25

    plt.bar(x - width, current_values, width, label='Current Value')
    plt.bar(x, targets, width, label='Target')
    plt.bar(x + width, stretch, width, label='Stretch Goal')

    plt.xlabel('Metrics')
    plt.ylabel('Value')
    plt.title('Performance Against Success Criteria')
    plt.xticks(x, metrics, rotation=45)
    plt.legend()

    plt.tight_layout()
    plt.savefig('success_criteria.png', dpi=300, bbox_inches='tight')
    plt.close()

if __name__ == "__main__":
    # Generate all visualizations
    create_bar_chart()
    create_response_time_chart()
    create_radar_chart()
    create_baseline_comparison()
    create_error_analysis()
    create_resource_utilization()
    create_success_criteria_chart()

    print("\nAll visualizations generated successfully!")

    # Export metrics to CSV for reproducibility
    df.to_csv('raw_benchmark_data.csv', index=False)
    pd.DataFrame([metrics]).to_csv('aggregated_metrics.csv', index=False)
    pd.DataFrame([error_metrics]).to_csv('error_metrics.csv', index=False)
    pd.DataFrame([resource_metrics]).to_csv('resource_metrics.csv', index=False)
    baseline_df.to_csv('baseline_comparison.csv', index=False)

    print("Benchmark data exported to CSV files for reproducibility")
