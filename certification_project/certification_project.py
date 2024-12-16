import argparse
from googlesearch import search

def google_search(query, num_results):
    for result in search(query, num=num_results, stop=num_results, pause=2):
        print(result)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Perform a Google search and return the top links.")
    parser.add_argument('query', type=str, help="The search query.")
    parser.add_argument('--num_results', type=int, default=10, help="Number of search results to return.")
    
    args = parser.parse_args()
    google_search(args.query, args.num_results)
