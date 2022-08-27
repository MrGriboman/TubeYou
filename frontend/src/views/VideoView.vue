<template>
  <HeaderView/>
  <main class="flex pt-20 sticky md-20">
    <div class="w-2/3 p-5 h">
      <div v-for="video in videos" :key="video.id" class="max-w-full">
        <video height="3840" width="2160" controls :src="`${video.video}`">
          <track kind="captions"/>
        </video>
        <div class="font-medium text-2xl ml-4">{{video.name}}</div>
        <div class="flex">
            <div class="ml-3 mr-1 mt-0.5">
              <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </div>
            <div class="mr-3">{{ video.views }}</div>
            <button class="ml-3 mr-1 mt-0.5" @click="isLiked = !isLiked">
              <svg class="w-5 h-5 fill-pink-300 active:fill-red-500" :class="{'fill-red-500': isLiked}" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </button>
            {{ video.likes + isLiked }}
        </div>
      </div>
    </div>
    <div class="w-1/3 p-5 overflow-auto h overflow-x-hidden">
      <div  v-for="other_video in others" :key="other_video.id" class="pb-5">
        <a :href="$router.resolve({name: 'video', params: {id: other_video.id}}).href">
          <div class="flex">
            <img :src="`${ other_video.preview}`" :alt="X" class="object-cover aspect-video h-3/5 w-3/5">
            <div class="m-auto w-1/3 font-mono underline">
              {{ other_video.name }}
            </div>
          </div>
          <div class="flex font-mono">
            <div class="ml-3 mr-1 mt-0.5">
              <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                <path d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z" />
              </svg>
            </div>
            <div class="mr-3">{{ other_video.views }}</div>
            <div class="ml-3 mr-1 mt-0.5">
              <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="pink" viewBox="0 0 24 24" stroke="currentColor">
                <path d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z" />
              </svg>
            </div>
            {{ other_video.likes }}
          </div>
        </a>

      </div>
    </div>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue';

export default {
  data() {
    return {
      videos: [],
      others: [],
      isLiked: false,
    };
  },
  async created() {
    console.log(this.$route.params.id);
    const request = 'http://127.0.0.1:8000/api/v1/mainvideos/?id=' + this.$route.params.id;
    const response = await fetch(request);
    this.videos = await response.json();
    const request1 = 'http://127.0.0.1:8000/api/v1/mainvideos/?neid=' + this.$route.params.id;
    const response1 = await fetch(request1);
    this.others = await response1.json();
  },
  components: {
    HeaderView,
  },
};

// Запрос на получение лайка от конкретного пользователя
</script>

<style>
.h{
  height: calc(100vh - 80px);
}
.button-active{
  @apply fill-red-300;
}
</style>
