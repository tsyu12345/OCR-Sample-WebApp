<script setup lang="ts">
import { onMounted, ref } from 'vue';

const videoElement = ref<HTMLVideoElement | null>(null);


const selectedCamera = ref<MediaDeviceInfo | null>(null);
const availableCameras = ref<MediaDeviceInfo[]>([]);

// カメラを起動する関数
const startCamera = async (deviceId: string) => {
    try {
        const stream = await navigator.mediaDevices.getUserMedia({
            video: {
                deviceId: deviceId,
                facingMode: 'environment',
                width: { ideal: 1270 },
                height: { ideal:  720 }
            }
        });
        if (videoElement.value) {
            videoElement.value.srcObject = stream;
        }
    } catch (error) {
        console.error('カメラにアクセスできません:', error);
    }
};

const initCameraSelection = async () => {
    const cameras = await getCamerasSrc();
    availableCameras.value = cameras;
};

const changeCamera = (camera: MediaDeviceInfo) => {
    selectedCamera.value = camera;
    startCamera(camera.deviceId);
};


const getCamerasSrc = async (): Promise<MediaDeviceInfo[]> => {
    try {
        const devices = await navigator.mediaDevices.enumerateDevices();
        const cameras = devices.filter((device) => device.kind === 'videoinput');
        console.log(cameras);
        return cameras;
    } catch (error) {
        console.error('カメラにアクセスできません:', error);
        return [];
    }
};


onMounted(async() => {
    //デフォルトでは最初に見つかったカメラを起動する
    await initCameraSelection();
    selectedCamera.value = availableCameras.value[0];
    startCamera(selectedCamera.value.deviceId);
});



</script>

<template>
    <div class="">
        <video id="camera" autoplay muted playsinline class="bg-black w-100 h-100" width="100%" height="100%" ref="videoElement"></video>
        <div class="row mt-3">
            <div class="col d-flex justify-content-center align-items-center">
                <button class="rounded-circle">
                    <svg xmlns="http://www.w3.org/2000/svg" width="50" height="50" fill="currentColor" class="bi bi-record" viewBox="0 0 16 16">
                        <path d="M8 12a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm0 1A5 5 0 1 0 8 3a5 5 0 0 0 0 10z"/>
                    </svg>
                </button>
            </div>
            <div class="dropdown mt-2">
                <button class="btn btn-secondary dropdown-toggle" type="button" data-bs-toggle="dropdown" aria-expanded="false">
                    {{ selectedCamera ? selectedCamera.label : 'カメラを選択'}}
                </button>
                <ul class="dropdown-menu" ref="cameraMenu">
                    <li v-for="camera in availableCameras" :key="camera.deviceId">
                        <a class="dropdown-item" href="#" @click="changeCamera(camera)">{{ camera.label }}</a>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>

<style scoped>
</style>