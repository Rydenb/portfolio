
comments: true
---

## As a conversation Starter
## About Me

Hi! My name is Ryden. I have lived in San Diego, California my whole life. Some of my biggest interests are video games, badminton, and soccer.

## Where I’m From

San Diego has always been home for me. I have grown up in the San Diego area and have lived here my whole life.

**California Flag**

San Diego, California<br>
Home my whole life

Here are some places I have lived.
## My Interests

<comment>
Flags are made using Wikipedia images
</comment>
Here are some of the things I enjoy:

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
    .interest-grid {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }
    .grid-item {

    .interest-card {
        overflow: hidden;
        border: 1px solid #ddd;
        border-radius: 10px;
        text-align: center;
        background: #fff;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.12);
    }
    .grid-item img {

    .interest-card img {
        width: 100%;
        height: 100px; /* Fixed height for uniformity */
        object-fit: contain; /* Ensure the image fits within the fixed height */
    }
    .grid-item p {
        margin: 5px 0; /* Add some margin for spacing */
    }

    .image-gallery {
        display: flex;
        flex-wrap: nowrap;
        overflow-x: auto;
        gap: 10px;
        }

    .image-gallery img {
        max-height: 150px;
        height: 180px;
        object-fit: cover;
        border-radius: 5px;
    }
</style>

<!-- This grid_container class is used by CSS styling and the id is used by JavaScript connection -->
<div class="grid-container" id="grid_container">
    <!-- content will be added here by JavaScript -->
</div>

<script>
    // 1. Make a connection to the HTML container defined in the HTML div
    var container = document.getElementById("grid_container"); // This container connects to the HTML div

    // 2. Define a JavaScript object for our http source and our data rows for the Living in the World grid
    var http_source = "https://upload.wikimedia.org/wikipedia/commons/";
    var living_in_the_world = [
        {"flag": "0/01/Flag_of_California.svg", "greeting": "Hey", "description": "California - forever"},
    ];

    // 3a. Consider how to update style count for size of container
    // The grid-template-columns has been defined as dynamic with auto-fill and minmax

    // 3b. Build grid items inside of our container for each row of data
    for (const location of living_in_the_world) {
        // Create a "div" with "class grid-item" for each row
        var gridItem = document.createElement("div");
        gridItem.className = "grid-item";  // This class name connects the gridItem to the CSS style elements
        // Add "img" HTML tag for the flag
        var img = document.createElement("img");
        img.src = http_source + location.flag; // concatenate the source and flag
        img.alt = location.flag + " Flag"; // add alt text for accessibility

        // Add "p" HTML tag for the description
        var description = document.createElement("p");
        description.textContent = location.description; // extract the description

        // Add "p" HTML tag for the greeting
        var greeting = document.createElement("p");
        greeting.textContent = location.greeting;  // extract the greeting
    .interest-card h3 {
        margin: 12px 8px 6px;
    }

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    .interest-card p {
        margin: 0 12px 14px;
    }
</script>
</style>


### My Interests

Some of my biggest interests are video games, badminton, and soccer.
    <div class="interest-card">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Badminton.jpg" alt="Badminton equipment">
        <h3>🏸 Badminton</h3>
        <p>I enjoy playing badminton in my free time.</p>
        <a href="https://commons.wikimedia.org/wiki/Category:Badminton" target="_blank" rel="noopener">Image source</a>
    </div>

- 🎮 Video Games
- 🏸 Badminton
- ⚽ Soccer
    <div class="interest-card">
        <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Soccer%20Ball%20%28120908768%29.jpg" alt="Soccer ball">
        <h3>⚽ Soccer</h3>
        <p>I enjoy playing soccer and staying active.</p>
        <a href="https://commons.wikimedia.org/wiki/File:Soccer_Ball_(120908768).jpg" target="_blank" rel="noopener">Image source</a>
    </div>
</div>

### Culture, Family, and Fun
## More About My Interests

Everything for me, as for many others, revolves around family and faith.
- 🎮 **Video Games**
- 🏸 **Badminton**
- ⚽ **Soccer** 
In my free time, I enjoy playing Rocket League, badminton, and soccer. San Diego has been my home my entire life, and many of my hobbies and interests have developed while growing up here.
