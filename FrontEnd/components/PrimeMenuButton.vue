<script setup lang="ts">

const props = defineProps({
    text: String,
    svg: String,
    onClick: Function,
})

const onHandleClick = () => {
    if(props.onClick) {
        props.onClick();
    }
}

</script>


<template>
<div class="w-fit border border-white rounded mx-auto p-1 px-2 btn-dark" @click="onHandleClick">
    <div v-html="svg"></div>
    <p class="">{{ props.text }}</p>
</div>
</template>

<style scoped></style>