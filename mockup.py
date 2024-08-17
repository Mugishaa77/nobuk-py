import pandas as pd

# Mock data for different categories
mock_data = {
    'Venue': [
        {'name': 'Small Hall', 'price': 5000, 'url': 'https://venue1.example.com'},
        {'name': 'Medium Hall', 'price': 8000, 'url': 'https://venue2.example.com'}
    ],
    'Food and Beverages': [
        {'name': 'Buffet', 'price': 6000, 'url': 'https://food1.example.com'},
        {'name': 'Catering Service', 'price': 7000, 'url': 'https://food2.example.com'}
    ],
    'Decorations': [
        {'name': 'Basic Decorations', 'price': 2000, 'url': 'https://decorations1.example.com'},
        {'name': 'Premium Decorations', 'price': 3000, 'url': 'https://decorations2.example.com'}
    ],
    'Entertainment': [
        {'name': 'DJ Service', 'price': 4000, 'url': 'https://entertainment1.example.com'},
        {'name': 'Live Band', 'price': 6000, 'url': 'https://entertainment2.example.com'}
    ],
    'Miscellaneous': [
        {'name': 'Photographer', 'price': 3000, 'url': 'https://miscellaneous1.example.com'},
        {'name': 'Party Favors', 'price': 1500, 'url': 'https://miscellaneous2.example.com'}
    ]
}

# Function to get the best options within the budget
def get_best_options(budget, category_data):
    all_options = []
    for category, options in category_data.items():
        affordable_options = [option for option in options if option['price'] <= budget]
        affordable_options = sorted(affordable_options, key=lambda x: x['price'])
        all_options.append({
            'category': category,
            'options': affordable_options
        })
    return all_options

# Function to summarize and recommend the best options
def summarize_and_recommend(options, budget):
    recommendations = []
    total_spent = 0
    
    for category_info in options:
        category = category_info['category']
        options = category_info['options']
        
        if options:
            best_option = options[0]  # The cheapest option
            recommendations.append(f"Category: {category}\nBest Option: {best_option['name']} at {best_option['price']} shillings (Available at {best_option['url']})")
            total_spent += best_option['price']
        else:
            recommendations.append(f"Category: {category}\nNo options available within the budget.")
    
    remaining_budget = budget - total_spent
    summary = f"Total Budget: {budget} shillings\nTotal Spent: {total_spent} shillings\nRemaining Budget: {remaining_budget} shillings\n"
    summary += "\n".join(recommendations)
    
    return summary

# Example usage
budget = 15000
best_options = get_best_options(budget, mock_data)
summary = summarize_and_recommend(best_options, budget)

print("Comprehensive Budget and Recommendations:")
print(summary)
