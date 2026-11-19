# CS360CourseProject

Info about/code for my course project in Bradley University's CS 360 Fundamentals of Data Science course. [BU CS Department Course Catalog](https://catalog.bradley.edu/undergraduate/course-descriptions/cs/)

## Project Overview from Course Material

This semester-long project is your opportunity to apply everything you’ve learned in a way that produces something portfolio; something you’d be proud to show to an employer or grad school. You’ll choose your own dataset, apply an appropriate combination of data cleaning, exploration, modeling, and interpretation techniques, and present your results during our final-exam slot.

## Dataset

I have chose this dataset from [Kaggle](https://www.kaggle.com/datasets/) for use in the project:
[🎬 Massive Rotten Tomatoes Movies & Reviews](https://www.kaggle.com/datasets/andrezaza/clapper-massive-rotten-tomatoes-movies-and-reviews?select=rotten_tomatoes_movies.csv)

This is a considerably large dataset (~1.4M rows), though it becomes smaller when considering that many movies have reviews from multiple critics.

The current plan is to group movies by their genres, compare statistics of the critic and audience reviews within that genre, and train a prediction model to answer how a new movie in a given genre might be rated by critics given its audience review, or vice versa?

### The current theoretical process (before any coding successes or failures)

1. Group movies by genre
2. Compare audience & critic reviews for every movie in genre training data
3. "Is critic review > audience review" (or vice versa) is boolean, could be used to generate probability to validate against test data

## Collaborators

- [aourbanek](https://github.com/aourbanek/) - Repository owner, Project Lead
- [DaveBrennanBradley](https://github.com/DaveBrennanBradley) - BU Course Instructor
