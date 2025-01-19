# *Search Algorithms: Binary and Linear Search*

## *Project Overview*

In this project, I have implemented two of the most fundamental search algorithms: *Linear Search* and *Binary Search*. These algorithms are used to locate specific elements in a list or array. By understanding the key differences between them, we gain insight into their efficiencies and use cases.

---

 *Code purpose*

The code performs two distinct searching algorithms:

- **Linear Search**: A method that checks each element one at a time, starting from the beginning of the list. It continues until the target element is found or the entire list is traversed.
- **Binary Search**: This search method requires the list to be sorted. It works by dividing the list into two halves, narrowing the search range based on whether the target is smaller or larger than the middle element. The search continues in this fashion until the target is found or the list is reduced to nothing.

---

 *Time Complexity Breakdown*

### **Linear Search**:
- **Best Case**: 
  - *O(1)* — The target element is found immediately at the *first position*.
  
- **Worst Case**: 
  - *O(n)* — The target element is either at the *last position* or is *not in the list* at all. Here, the algorithm has to check every element, resulting in linear time complexity.

---

### **Binary Search**:
- **Best Case**: 
  - *O(1)* — The element is found in the *middle* of the list, minimizing the search effort.
  
- **Worst Case**: 
  - *O(log n)* — In this case, Binary Search performs efficiently, even on large sorted datasets. Each iteration of the search cuts the list in half, making the search exponentially faster than linear search.

However, if the list is *unsorted*, Binary Search loses its advantage, and the time complexity becomes *O(n)* because the list would need to be scanned entirely before sorting.

---

 *How to Use the Program*

To get started with this project, follow these simple steps:

1. *Clone the repository* to your local machine to get the project files.
2. *Navigate to the project directory* using your terminal or file explorer.
3. *Run the program* using the command provided.
4. *Input a list of numbers* when prompted by the program.
5. Enter the *target value* you want to search for.
6. The program will display:
   - The index of the target if it is found.
   - A message indicating that the target is not in the list if the search fails.
7. We can also run program on online compilor (programiz).
8. On programiz we can easily run any program.

---

 *What I Learned From This Project*

Working on this project was a rewarding experience, as it allowed me to dive deeper into the *mechanics of search algorithms* and *optimize their performance*.

- *Linear Search* is simple to implement and understand, but its major drawback is inefficiency. In large datasets, it becomes slow because it has to check each element one by one. Its worst-case time complexity is *O(n)*, making it unsuitable for larger data.
  
- *Binary Search* is a much more powerful algorithm, especially when dealing with large *sorted datasets*. Its worst-case time complexity is *O(log n)*, meaning it’s significantly faster than Linear Search. However, its dependency on the list being sorted makes it less versatile compared to Linear Search.

Overall, this project improved my problem-solving skills by requiring me to think critically about how to *optimize searching operations* and how to handle different types of data efficiently.

You can view the project and details about its implementation on my https://www.linkedin.com/posts/faisal-khurshid-31b960347_softwaredevelopment-algorithms-learningbydoing-activity-7286617110569443331-Us64?utm_source=share&utm_medium=member_desktop.

---
