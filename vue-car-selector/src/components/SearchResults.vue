<template>
  <div class="results-container">
    <div class="section-title">
      YOUR TAILORED RECOMMENDATION
      <div class="subtitle">We have found {{ countCars }} cars that you may like</div>
      <div class="subtitle" v-if="countCars>5"><small>(The top 5 of them are most suited to your needs)</small></div>
    </div>
    <div class="results">
      <car-result-item
          v-for="(car, index) in carList"
          :key="car.id"
          :class="{'gray-mask': index >= 5}"
          class="car-item"
          :modelInfo="car"/>
    </div>
    <div v-if="isLoading" class="center-content">
      <div class="lds-hourglass"></div>
    </div>
    <div class="button-container" v-if="carList.length !== countCars">
      <button class="show-car-button" @click="page+=1">
        Load more
      </button>
    </div>
  </div>
</template>

<script setup>
import {defineProps, onBeforeMount, ref, watch} from "vue";
import {CarsService} from "../api";
import CarResultItem from "./CarResultItem";

defineProps(['form'])
const countCars = ref(null)
const carList = ref([])
const page = ref(1)
const isLoading = ref(false)
import {useAppStore} from "../store";

const appStore = useAppStore();

const makeRequest = async () => {
  isLoading.value = true;
  const form = {...appStore.form, page: page.value};
  const response = await CarsService.getCars(form);
  countCars.value = response.count;
  carList.value.push(...response.results);
  isLoading.value = false;
}


watch(page, async () => {
  await makeRequest();
})

onBeforeMount(async () => {
  await makeRequest();
})
</script>

<style scoped lang="less">
.results-container {
  position: relative;
}

.results {
  display: flex;
  flex-wrap: wrap;
  justify-content: space-between;
  margin-top: 30px;

  .car-item {
    width: calc(50% - 15px);
    margin-bottom: 30px;
  }
}

.section-title {
  font-size: 30px;
  font-weight: 800;

  .subtitle {
    font-size: 15px;
  }
}

.button-container {
  display: flex;
  justify-content: center;
}

.gray-mask {
  position: relative;
}

.gray-mask::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  background: rgba(106, 106, 106, 0.6); /* Półprzezroczysta czarna maska; zmień kolor tła na szary, jeśli potrzebujesz */
  z-index: 1;
}

.show-car-button {
  cursor: pointer;
  padding: 10px 40px;
  font-weight: 900;
  margin: 20px 0;
  color: white;
  font-size: 15px;
  outline: rgba(0, 0, 0, 0.2) 3px solid;
  border: none;
  background: linear-gradient(rgba(215, 29, 128, 1), rgba(196, 44, 140, 1)) !important;
}

</style>