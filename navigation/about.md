---
layout: post
<<<<<<< HEAD
title: About Me
=======
title: About
>>>>>>> upstream/main
permalink: /about/
comments: true
---

<<<<<<< HEAD
## As a Conversation Starter

## About Me

Hi! My name is **Ryden**. I have lived in **San Diego, California** my whole life. Some of my biggest interests are **video games, badminton, and soccer**.

## Where I'm From

San Diego has always been home for me. I have grown up in the San Diego area and have lived here my whole life. ewfji

<style>
    .location-container {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 24px;
        margin: 20px 0;
    }

    .location-item {
        text-align: center;
    }

    .location-item img {
        width: 180px;
        height: 110px;
        object-fit: contain;
    }

    .heritage-flag {
        display: flex;
        width: 180px;
        height: 110px;
        margin: 0 auto;
        overflow: hidden;
    }

    .heritage-flag img {
        width: 50%;
        height: 100%;
        object-fit: cover;
    }

    .interest-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(220px, 1fr));
        gap: 20px;
        margin: 20px 0;
    }

    .interest-card {
        overflow: hidden;
        border: 1px solid #303846;
        border-radius: 10px;
        text-align: center;
        background: #171c25;
        color: #f5f7fa;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
    }

    .interest-card img {
        width: 100%;
        height: 150px;
        object-fit: cover;
    }

    .interest-card h3 {
        margin: 12px 8px 6px;
        color: #ffffff;
    }

    .interest-card p {
        margin: 0 12px 14px;
        color: #c8d0dc;
    }

    .interest-card a {
        display: inline-block;
        margin-bottom: 14px;
    }
</style>

<div class="location-container">
    <div class="location-item">
        <img src="https://upload.wikimedia.org/wikipedia/commons/0/01/Flag_of_California.svg" alt="California Flag">
        <p><strong>San Diego, California</strong></p>
        <p>Home my whole life</p>
    </div>
    <div class="location-item">
        <div class="heritage-flag">
            <img src="https://upload.wikimedia.org/wikipedia/en/9/9e/Flag_of_Japan.svg" alt="Japanese flag">
            <img src="https://upload.wikimedia.org/wikipedia/commons/a/a4/Flag_of_the_United_States.svg" alt="United States flag">
        </div>
        <p><strong>Japanese / White</strong></p>
        <p>Half Japanese, half American</p>
    </div>
</div>

## My Interests

Some of the things I enjoy:

<div class="interest-grid">

<div class="interest-card">
    <img src="https://upload.wikimedia.org/wikipedia/commons/e/e0/Rocket_League_coverart.jpg" alt="Rocket League cover art">
    <h3>Video Games</h3>
    <p>I enjoy playing video games, especially Rocket League, and playing with friends.</p>
</div>

<div class="interest-card">
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Badminton.jpg" alt="Badminton">
    <h3>Badminton</h3>
    <p>I enjoy playing badminton in my free time, especially with friends.</p>
</div>

<div class="interest-card">
    <img src="https://commons.wikimedia.org/wiki/Special:FilePath/Soccer%20Ball%20%28120908768%29.jpg" alt="Soccer Ball">
    <h3>Soccer</h3>
    <p>I enjoy playing soccer and staying active.</p>
</div>
</div>

## A Little More About Me

A lot of my free time is spent playing sports, going to the gym, or playing games with friends. I enjoy playing badminton and soccer, as well as playing video games like Rocket League.

I'm also really interested in technology. I enjoy programming and building projects, but I also like exploring new technologies and figuring out how things work.

San Diego has been my home my entire life, and many of my hobbies and interests have developed while growing up here.
=======
## As a conversation Starter

Here are some places I have lived.

<comment>
Flags are made using Wikipedia images
</comment>

<style>
    /* Style looks pretty compact, 
       - grid-container and grid-item are referenced the code 
    */
    .grid-container {
        display: grid;
        grid-template-columns: repeat(auto-fill, minmax(150px, 1fr)); /* Dynamic columns */
        gap: 10px;
    }
    .grid-item {
        text-align: center;
    }
    .grid-item img {
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
        {"flag": "b/b9/Flag_of_Oregon.svg", "greeting": "Hi", "description": "Oregon - 9 years"},
        {"flag": "b/be/Flag_of_England.svg", "greeting": "Alright mate", "description": "England - 2 years"},
        {"flag": "e/ef/Flag_of_Hawaii.svg", "greeting": "Aloha", "description": "Hawaii - 2 years"},
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

        // Append img and p HTML tags to the grid item DIV
        gridItem.appendChild(img);
        gridItem.appendChild(description);
        gridItem.appendChild(greeting);

        // Append the grid item DIV to the container DIV
        container.appendChild(gridItem);
    }
</script>

### Journey through Life

Here is what I did at those places

- 🏫 Lots of Elementary Schools in Tucson, LA, Honolulu, and Glendale (CA)
- 🏫 Middle and High School in Glendale (CA), Hoover High graduated '77
- 🎓 Glendale CA Community College, UCLA Extension, LA Wilshire Computer Tech School '77 to '79
- ⛪ England, London Missionary for Church of Jesus Christ of Latter-day Saints '79 to '81
- 💼 Culver City, Glendale CA founder at Ashton-Tate, original PC's dBase 2 and 3 '82 to '87
- 🎓 Eugene Oregon Undergraduate CompSci Degree at University of Oregon (Go Ducks!) '89 to '91
- 💼 Eugene Oregon, founder and owner @ Microniche `88, Point Control CAD CAM developer '91 to '96
- 🏢 San Diego CA Qualcomm, Satellite Comm and 1st Mobile OS (BREW) '96 to '19
- 👨‍🏫 San Diego CA Teacher of Computer Science @ Del Norte High School San Diego '19 to present

### Culture, Family, and Fun

Everything for me, as for many others, revolves around family and faith.

- My mother told me that I was Danish, English. and Irish, here is my researched [family tree]({{site.baseurl}}/images/about/familytree.png)
- My family is pretty big as I have been married twice, my 1st wife passed away.  We have had 5 kids, 4 adopted by me, 1 biological.  Plus, there are three grandkids.  My name to my grandkids is Abuilito.
- The gallery of pics has some of my family, fun, culture and faith memories.

<comment>
Gallery of Pics, scroll to the right for more ...
</comment>
<div class="image-gallery">
  <img src="{{site.baseurl}}/images/about/missionary.jpg" alt="Image 1">
  <img src="{{site.baseurl}}/images/about/john_tamara.jpg" alt="Image 2">
  <img src="{{site.baseurl}}/images/about/tamara_fam.jpg" alt="Image 3">
  <img src="{{site.baseurl}}/images/about/surf.jpg" alt="Image 4">
  <img src="{{site.baseurl}}/images/about/john_lora.jpg" alt="Image 5">
  <img src="{{site.baseurl}}/images/about/lora_fam.jpg" alt="Image 6">
  <img src="{{site.baseurl}}/images/about/lora_fam2.jpg" alt="Image 7">
  <img src="{{site.baseurl}}/images/about/pj_party.jpg" alt="Image 8">
  <img src="{{site.baseurl}}/images/about/trent_family.png" alt="Image 9">
  <img src="{{site.baseurl}}/images/about/claire.jpg" alt="Image 10">
  <img src="{{site.baseurl}}/images/about/grandkids.jpg" alt="Image 11">
  <img src="{{site.baseurl}}/images/about/farm.jpg" alt="Image 12">
</div>
>>>>>>> upstream/main
