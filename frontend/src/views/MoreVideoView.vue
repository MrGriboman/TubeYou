<template>
  <main>
    <div class="bg-amber-800 justify-end pt-20 w-1/3">
      fgfd
    </div>
    <div class="pt-20 grid-cols-1">
      <div v-for="video in videos" :key="video.id" class="w-20">
        <div class="relative mb-3">
          <router-link :to="{name: 'video', query: {id: video.id}}" >
            <img :src="`${ video.preview}`" :alt="X" class="object-cover aspect-video">
          </router-link>
        </div>
      </div>
    </div>
  </main>
</template>

<script>

export default {
  data() {
    return {
      videos: [],
    };
  },
  async created() {
    const response = await fetch('http://localhost:8000/api/v1/mainvideos?amount=10');
    this.videos = await response.json();
  },
};
</script>

<style>

</style>
