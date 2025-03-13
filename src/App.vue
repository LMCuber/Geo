<template>
	<div id="map">
		<div id="map-grid">
			<img v-for="image in getImages()" :src="image">
		</div>

		<span>{{ year }}</span>
		<input id="time-slider" type="range" v-model="year" min="-3000" max="2022" step="1" />

		<button @click="getPositions()">GETPOS</button>
	</div>
</template>


<script setup>

import { ref } from "vue"

const year = ref(1800)
const defaultImage = "/maps/default.png"
let imageCache = {};

function getImages() {
	if (imageCache[year.value]) {
		return imageCache[year.value]
	} else {
		let images = [];
		let valid_year = year.value;

		for (let y = 0; y <= 2; y++) {
			for (let x = 0; x <= 3; x++) {
				valid_year = Math.min(Math.max(valid_year - 1, -3000), 2022);

				let year_str = valid_year.toString().replace("-", "B");
				let path = `/maps/${year_str}/${year_str}_${y}_${x}.png`;
				while (fetch(path).status != 200) {
					console.log("File not found:", path);
					valid_year--;

					year_str = valid_year.toString().replace("-", "B");
					path = `/maps/${year_str}/${year_str}_${y}_${x}.png`
				}
				images.push(path);
			}
		}

		imageCache[year] = images;
		return images;
	}
}

function loadDefaultImage(e) {
	e.target.src = defaultImage;
}

function getPositions() {
	console.log(year.value);
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
