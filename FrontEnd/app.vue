<script setup lang="ts">
import { ref } from 'vue';

const librarys = ref([
  'Easy OCR', 
  'Paddle OCR', 
  'Google Cloud Vision',
]);
const selected = ref(librarys.value[0]);
const cameraMode = ref(false);
const recognitionMode = ref(false);

const changeLibName = (e: Event) => {
  const target = e.target as HTMLAnchorElement;
  selected.value = target.innerText;
}

const takePicture = () => {
  console.log('takePicture');
  cameraMode.value = true;
  recognitionMode.value = false;
  //ネイティブのカメラを起動して写真を撮影する
  const input = document.createElement('input');
}

const fileUpload = () => {
  console.log('fileUpload');
  recognitionMode.value = true;
  cameraMode.value = false;
}

</script>

<template>
  <div id="container" class="h-screen text-center text-bg-dark">
    <header class="w-100 mb-5">
      <h1 class="text-light mx-auto pt-4">OCR</h1>
      <ul class="nav justify-content-center">
        <li class="nav-item">
          <a class="nav-link text-light" aria-current="page" href="#">GitHub</a>
        </li>
        <li class="nav-item">
          <a class="nav-link text-light" href="#">Docs</a>
        </li>
      </ul>
    </header>
    <div class="container">
      <div class="row">
        <div class="col">
          <div class="btn-group">
            <button class="btn btn-secondary btn-lg-md" type="button">
              {{ selected }}
            </button>
            <button type="button" class="btn btn-lg-md btn-secondary dropdown-toggle dropdown-toggle-split"
              data-bs-toggle="dropdown" aria-expanded="false">
            </button>
            <ul class="dropdown-menu">
              <li v-for="library in librarys" :key="library">
                <a class="dropdown-item" href="#" @click="changeLibName">{{ library }}</a>
              </li>
            </ul>
          </div>
        </div>
      </div>
      <div class="row d-flex justify-content-center mt-3">
        <div class="col">
          <div id="camera" class="w-fit border border-white rounded mx-auto p-1 px-2 btn-dark" @click="takePicture">
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-camera-fill"
              viewBox="0 0 16 16">
              <path d="M10.5 8.5a2.5 2.5 0 1 1-5 0 2.5 2.5 0 0 1 5 0z"/>
              <path d="M2 4a2 2 0 0 0-2 2v6a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2h-1.172a2 2 0 0 1-1.414-.586l-.828-.828A2 2 0 0 0 9.172 2H6.828a2 2 0 0 0-1.414.586l-.828.828A2 2 0 0 1 3.172 4H2zm.5 2a.5.5 0 1 1 0-1 .5.5 0 0 1 0 1zm9 2.5a3.5 3.5 0 1 1-7 0 3.5 3.5 0 0 1 7 0z" />
            </svg>
            <p class="">カメラから撮影</p>
          </div>
        </div>
        <div class="col">
          <div id="fileup" class="w-fit border border-white rounded mx-auto p-1 px-2 btn-dark" @click="fileUpload">
            <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-image-fill"
              viewBox="0 0 16 16">
              <path
                d="M.002 3a2 2 0 0 1 2-2h12a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2h-12a2 2 0 0 1-2-2V3zm1 9v1a1 1 0 0 0 1 1h12a1 1 0 0 0 1-1V9.5l-3.777-1.947a.5.5 0 0 0-.577.093l-3.71 3.71-2.66-1.772a.5.5 0 0 0-.63.062L1.002 12zm5-6.5a1.5 1.5 0 1 0-3 0 1.5 1.5 0 0 0 3 0z" />
            </svg>
            <p class="">画像から選択</p>
          </div>
        </div>
      </div>
      <div class="row">
        <div class="col"></div>
      </div>
    </div>
  </div>
</template>



<script lang="ts">
export default {
  head: {
    bodyAttrs: {
      class: 'bg-dark w-screen h-screen text-light'
    }
  }
}
</script>

<style scoped>

.w-fit {
  width: fit-content;
}

.h-screen {
  height: 100vh;
}

</style>
