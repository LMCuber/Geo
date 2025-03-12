<template>
  
  <div id="map">
    <div id="map-grid">
      <img v-for="image in getImages()" :src="image" @error="loadDefaultImage">
    </div>

    <span>{{ year }}</span>
    <input id="time-slider" type="range" v-model="year" min="-3000" max="2022" step="1"/>

    <!-- <button @click="console.log(getImages())">GETIM</button> -->

  </div>

</template>


<script setup>

  import { ref } from "vue"

  const year = ref(2022)
  const defaultImage = "/maps/default.png"
  var imageCache = {};

  function getImages() {
    if (year.value in imageCache) {
      return imageCache[year.value]
    } else {
      var images = [];
      for (let y = 0; y <= 2; y++) {
        for (let x = 0; x <= 3; x++) {
          let file_name = `${year.value}_${y}_${x}.png`;
          let file_path = `/maps/${year.value}/` + file_name;
          // console.log("Loaded " + file_path);
          images.push(file_path);
        }
      }
      imageCache[year.value] = images;
      return images;
    }
  }

  function loadDefaultImage(e) {
    e.target.src = defaultImage;
  }

</script>


<style scoped>
  * {
    font-family: "Roboto mono", monospace;
  }

  #map {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 100vh;
  }
    
  #map span {
    font-size: 40px;
  }

  #time-slider {
    width: 800px;
  }

  #map-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    grid-template-rows: repeat(3, 1fr);
  }

  #map-grid img {
    width: 300px;
    height: auto;
    object-fit: cover;
    background-color: #99B3CC;
  }

</style>
