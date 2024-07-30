import unittest
from datetime import datetime
from scholarly import scholarly

from updatedScholarlyFile import get_author_info, extract_coauthors

class TestScholarly(unittest.TestCase):
    def setUp(self):
        # Test data for different authors
        self.authors = {
            "Dennis DeCoste": {
                "years": 1,
                "expected_coauthors": {
                    'Sean Lie', 'Shreyas Saxena', 'William Marshall', 'Joel Hestness', 'Tianda Li', 
                    'Vitaliy Chiley', 'Abhay Gupta', 'Vithursan Thangarasa', 'Kevin Leong', 'Anshul Samar'
                },
                "expected_papers": {
                    "SPDF: Sparse pre-training and dense fine-tuning for large language models": {
                        'Sean Lie', 'Shreyas Saxena', 'William Marshall', 'Tianda Li', 
                        'Kevin Leong', 'Abhay Gupta', 'Vithursan Thangarasa'
                    },
                    "RevBiFPN: the fully reversible bidirectional feature pyramid network": {
                        'Anshul Samar', 'Joel Hestness', 'Abhay Gupta', 
                        'Vitaliy Chiley', 'Vithursan Thangarasa'
                    }
                }
            },
            "Scott Shenker": {
                "years": 0,
                "expected_coauthors": {
                    'Ethan Katz-Bassett', 'Marjory Blumenthal', 'Wei-Lin Chiang', 'Ion Stoica', 
                    'Suryaprakash Vengadesan', 'Zongheng Yang', 'Justin Chang', 'Tejas Narechania', 
                    'Zhanghao Wu', 'Zhihong Luo', 'Amy Ousterhout', 'Dev Bali', 'Arvind Krishnamurthy', 
                    'Emmanuel Amaro', 'Nick Merrill', 'Eric Friedman', 'Ziming Mao', 'Siyuan Zhuang', 
                    'Aurojit Panda', 'Sylvia Ratnasamy', 'Ramesh Govindan', 'Romil Bhardwaj', 
                    'James McCauley', 'Sam Son', 'Michael Luo'
                },
                "expected_papers": {
                }
            }
        }

    def test_coauthors_extraction(self):
        # Test the co-authors extraction function
        for author_name, data in self.authors.items():
            author_info = get_author_info(author_name)
            self.assertIsNotNone(author_info, f"Author info should not be None for {author_name}")
            paper_coauthors_dict = extract_coauthors(author_info, data["years"])

            all_coauthors = set()
            for coauthors in paper_coauthors_dict.values():
                all_coauthors.update(coauthors)

            self.assertEqual(all_coauthors, data["expected_coauthors"], 
                             f"Co-authors for {author_name} do not match the expected output")

            for paper, coauthors in data["expected_papers"].items():
                self.assertIn(paper, paper_coauthors_dict, 
                              f"Paper '{paper}' not found in the extracted papers for {author_name}")
                self.assertEqual(paper_coauthors_dict[paper], coauthors, 
                                 f"Co-authors for paper '{paper}' do not match the expected output")

if __name__ == '__main__':
    unittest.main()
