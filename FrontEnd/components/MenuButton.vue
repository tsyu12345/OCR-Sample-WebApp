<script setup lang="ts">
import { defineComponent } from 'vue';

const props = defineProps({
    text: String,
    icon: HTMLElement,
    onClick: Function,
})

</script>


<template>
    <div class="w-fit border border-white rounded mx-auto p-1 px-2 btn-dark" @click="props.onClick">
        <!--props.iconを挿入したい-->
        <p class="">{{ props.text }}</p>
    </div>
</template>

<style scoped></style>