<template>
  <div>
    <div class="models_results">
      <div class="model_view">
        <div class="model_img">
          <div v-if="modelInfo.thumbnail" class="img" v-bind:style="modelImg"></div>
          <div v-else class="img"
               style="background: url('https://via.placeholder.com/800x500') no-repeat center;"></div>
          <div class="model_name"><span>{{ modelInfo.name }}</span></div>
        </div>
        <button @click="viewSubModel" class="btn_view">VIEW CAR DETAILS</button>
      </div>
    </div>
  </div>
</template>

<script>
import {OpenAPI} from "../api";

export default {
  name: "ModelCar",
  props: ['modelInfo',],
  data() {
    return {}
  },
  methods: {
    viewSubModel() {
      this.$router.push({name: 'carDetailsView', params: {carId: this.modelInfo.id}})
    }
  },
  computed: {
    modelImg: function () {
      return {
        background: `url(${OpenAPI.BASE}/media/${this.modelInfo.thumbnail}) no-repeat center`,
        backgroundSize: 'cover'
      }
    }
  }
}
</script>

<style scoped>
.model_view .img {
  width: 100%;
  min-height: 230px;
  margin-bottom: 5px;
  background-size: cover;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
}

.model_view {
  min-width: 100%;
}

.model_view .model_img {
  position: relative;
}

.model_view .model_img .model_name {
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  justify-content: center;
  text-align: center;
  align-items: center;
  padding: 4px;
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 35px;
  font-weight: 700;
  font-size: 15px;
}

.model_view .btn_view {
  width: 100%;
  height: 40px;
  background: rgba(255, 255, 255, 0.1);
  border: none;
  color: white;
  font-weight: 800;
  font-size: 16px;
}

.model_view .btn_view:hover {
  opacity: 1;
  background: linear-gradient(rgba(215, 29, 128, 0.8), rgba(196, 44, 140, 0.8)) !important;
  cursor: pointer;
}
</style>