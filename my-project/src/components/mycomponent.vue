<template>
    <div class="my-component">
        <h1>{{ message }}</h1>
    </div>

</template>

<script>
export default {
    name:'my-component',
    data(){
        return {
            message: 'Hello world'
        }
    }

}
</script>