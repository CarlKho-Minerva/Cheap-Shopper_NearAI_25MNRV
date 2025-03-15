import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
    'task_completed': [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
}

# Convert to DataFrame
df = pd.DataFrame(raw_data)

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

if __name__ == "__main__":
    # Generate all visualizations
    create_bar_chart()
    create_response_time_chart()
    create_radar_chart()

    print("\nVisualizations generated successfully!")
