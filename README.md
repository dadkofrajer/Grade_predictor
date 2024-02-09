# Grade Predicotr
#### Video Demo:  <https://youtu.be/PtdAqmZuN6g>
#### Description:


# Grade Calculator Web Application ## Overview This Flask web application acts as a grade calculator to help students determine the semester exam grade they need to achieve the desired average in a course
 This application manages different grading scenarios based on the number of grade categories and  presence or absence of semester exams


 ## Features - **Calculation Logic: ** The application calculates the required semester exam grade  based on user input such as  number of grade categories, exam attendance, and target average
 - **Scenario Management: ** Different HTML templates are provided for different assessment scenarios, ensuring a customized user experience based on the selected options
 - **Feasibility Check: ** The application checks the feasibility of achieving the desired average and provides appropriate feedback to the user


 ## Global Variables The following global variables are used to store input values ​​and intermediate calculations: - 'gt', 'g1', 'g2', 'g3', 'g4'
 ': variables to store note values ​​from different categories
 - 'gsum':  Sum of grade values ​​ from selected categories
 - 'grade_average': Target average of user input
 - 'Groups': Number of memo categories is
 - 'Exam': Existence of semester exam


 ## Routes - **'/' (index): ** Render the main input form so the user can select the number of groups, indicate whether they are checked, and enter the  target averag
 - **'/four_y', '/three_y', '/three_n', '/two_y', '/two_n', '/one_y', '/one_n': ** Roots for different scoring scenarios, Processing Notes Entering categories and rendering corresponding templates


 ## 'calculate()' Function The 'calculate()' function processes user input and calculates the required semester exam grade
 It considers different scenarios and provides corresponding grades and feedback text


 ## Usage 1
 Run your Flask application using Python app.py
 2
 Access the application via a web browser
 3
 Enter the number of groups, number of test participants, and target average value
 4

## Stylesheet

The application uses a custom stylesheet to enhance its visual appeal and user experience. Here is a brief description of the key styling elements:

### Header Styling

- **Background Color:** The header has a background color of `#477fff`, providing a distinctive and vibrant look.
- **Text Color:** The text within the header is set to white (`#fff`) for high contrast and readability.
- **Margin and Padding:** The header has a margin-bottom of `2rem` for spacing and padding of `2rem` at the top and `1rem` at the bottom for better alignment.
- **Text Alignment:** The text within the header is centered for a neat appearance.

### Body Styling

- **Background Color:** The body has a background color of `#4770ff`, complementing the header color and maintaining a cohesive theme.
- **Text Color:** The default text color is set to `#212529` for legibility against the background.
- **Font Settings:** The application uses a base font size of `1rem` with a weight of `400` and a line height of `1.5` for comfortable reading.
- **Text Alignment:** The main text is left-aligned for ease of reading.

### Container Styling

- **Margin and Padding:** The container has auto margins on the left and right, providing a centered layout. It also has padding on both sides to ensure content doesn't touch the edges.

### Link Styling

- **Color:** Links are styled in red for a noticeable and consistent appearance.

### Submit Button Styling

- **Size:** The submit button has a width of `20%` and a height of `100%`, ensuring it stands out and is easily clickable.

### Heading Styling

- **Text Alignment:** Headings (`h1`) are centered, creating a visually pleasing and organized structure.

## Features

- **Responsive Design:** The application features a responsive design with a centered header, ensuring a visually appealing layout.

- **Stylish Interface:** The stylesheet is designed with a cohesive color scheme, enhancing readability and providing a modern look.

- **Form Elements:** The input forms and buttons are styled for a consistent and user-friendly experience, aligning with the overall theme of the application.
