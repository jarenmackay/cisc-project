[Project_README_template.md](https://github.com/user-attachments/files/26698451/Project_README_template.md)
# Algorithm Name

## Demo video/gif/screenshot of test

## Problem Breakdown \& Computational Thinking

(You can add a flowchart and write the four pillars of computational thinking briefly in bullets)

## Steps to Run

## Hugging Face Link

## Author \& AI Acknowledgment



I am building an app that sorts a list of songs based on their song duration. This helps users organize their tracks from shortest to longest to create a better flow for a mix.

I chose Quick Sort because it uses a highly efficient "Divide and Conquer" approach. It fits this problem because it can quickly handle numerical data like song lengths by partitioning the list around a pivot duration.



Decomposition:

To solve this, I broke the task into these smaller steps:

Input Parsing - Taking a raw string of song data and converting it into a list of dictionaries (Title and Duration)

Pivot Selection - Choosing a song length to act as the "middle ground" for comparisons.

Partitioning - Moving songs shorter than the pivot to the left and longer ones to the right.

Recursive Sorting - Repeating this process on the smaller sub lists until the entire playlist is ordered.



Pattern Recognition:

I identified that the algorithm repeatedly performs the same comparison and swap operations. Regardless of how many songs are in the list, the "Pick Pivot -> Compare -> Partition" cycle repeats until the base case is reached.



Abstraction:

To keep the app "beginner friendly," I made the following choices:

Show - The user sees the song titles and their durations moving into their sorted positions.

Hide - I hid the complex index math, the recursive function calls, and the internal memory management from the GUI to avoid clutter.



Algorithm Design:

Input - User enters song names and lengths into a Gradio Textbox.

Validation - The app checks if durations are valid numbers; if not, it shows an error.

Process - The quick sort function partitions the data based on the duration key.

Output - The Gradio interface displays the final sorted playlist and a log of the simulation steps.



Flowchart:

Start: User enters a list of songs and durations.

Input Parsing: Convert raw text into a list of dictionaries.

Base Case: Is the list length 1 or 0?

Yes: Return list (Done).

No: Continue.

Pivot Selection: Pick the middle song as the pivot.

Partition: Compare each song's duration to the pivot.

Move "Shorter" to the Left.

Move "Longer" to the Right.

Recursive Step: Repeat the sort on the Left and Right sub-lists.

Combine: Merge \[Sorted Left + Pivot + Sorted Right].

Output: Display the final ordered list in Gradio.



Steps to Run:

\## Steps to Run (Local)

1\. \*\*Clone the repository:\*\* `git clone https://github.com/jarenmackay/cisc-project`

2\. \*\*Navigate to the folder:\*\*

&#x20;  `cd cisc project`

3\. \*\*Install dependencies:\*\*

&#x20;  `pip install -r requirements.txt`

4\. \*\*Run the application:\*\*

&#x20;  `python app.py`

5\. \*\*Access the UI:\*\*

&#x20;  Open the local URL in your web browser.



Hugging Face Link:





Testing and Verification:

I tested the app with the following cases:

Typical case - A list of 5 songs with varying lengths (ex 120s, 300s, 180s).

Edge Case (Empty) - Entering nothing; the app provides a "No data" message.

Edge Case (Duplicates) - Two songs with the exact same length (ex both 120s); the app maintains their relative order.

Bad Input - Typing "five minutes" instead of 300; the app triggers an error message.



Author: Jaren MacKay

AI Use: Assisted with structuring the README

