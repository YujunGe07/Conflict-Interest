from datetime import datetime
from scholarly import scholarly

def get_author_info(author_name):
    """
    Retrieve detailed author information using the scholarly module.
    
    Parameters:
    author_name (str): The name of the author to search for.
    
    Returns:
    dict: Filled author information dictionary if found, otherwise None.
    """
    search_query = scholarly.search_author(author_name)
    try:
        author = next(search_query)
        return scholarly.fill(author)
    except StopIteration:
        print(f"No author found for name: {author_name}")
        return None
    except Exception as e:
        print(f"Error retrieving author info: {e}")
        return None

def extract_coauthors(author_info, years):
    """
    Extract co-authors of the given author within a specified number of years.
    
    Parameters:
    author_info (dict): The author information dictionary.
    years (int): The number of years to look back for co-authorship.
    
    Returns:
    dict: Dictionary with paper titles as keys and sets of co-authors as values.
    """
    current_year = datetime.now().year
    paper_coauthors_dict = {}

    def get_pub_year(pub):
        """
        Extract the publication year from a publication dictionary.
        
        Parameters:
        pub (dict): The publication dictionary.
        
        Returns:
        int: The publication year.
        """
        try:
            return int(pub['bib'].get('pub_year', 0))
        except ValueError:
            return 0


    # Sort the publications based on years
    sorted_pubs = sorted(author_info['publications'], key=get_pub_year, reverse=True)
    for pub in sorted_pubs:
        pub_year = get_pub_year(pub)
        if pub_year and isinstance(pub_year, int) and current_year - pub_year <= years:
            try:
                filled_pub = scholarly.fill(pub)
                paper_title = filled_pub['bib'].get('title', 'No title')
                authors = filled_pub['bib'].get('author', '')
                if authors:
                    coauthors = set(authors.split(' and '))
                    coauthors.discard(author_info['name'])
                    paper_coauthors_dict[paper_title] = coauthors
            except Exception as e:
                print(f"Error filling publication: {e}")
        # Stop processing if we have moved out of the relevant years
        elif pub_year and isinstance(pub_year, int) and current_year - pub_year > years:
            break

    return paper_coauthors_dict

def main():
    author_name = input("Enter the author's name: ")
    years = int(input("Enter the number of years to look back for co-authorship: "))

    author_info = get_author_info(author_name)
    if author_info:
        print(f"Found author: {author_info['name']}")
        paper_coauthors_dict = extract_coauthors(author_info, years)
        all_coauthors = set()
        for coauthors in paper_coauthors_dict.values():
            all_coauthors.update(coauthors)

        print(f"Co-authors in the last {years} years: {all_coauthors}")
        print("Details:")
        for paper, coauthors in paper_coauthors_dict.items():
            print(f"Paper: {paper}")
            print(f"  Co-authors: {', '.join(coauthors)}")
    else:
        print(f"Unable to retrieve information for author: {author_name}")

if __name__ == "__main__":
    main()
