<template>
  <HeaderView/>
  <AsideView/>
  <ChannelView/>
  <main class="md:ml-24 xl:ml-64 pt-10 px-5 pb-5">
    <div class="flex">
      <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
        <path strokeLinecap="round" strokeLinejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
      </svg>
      <textarea class="pl-6">Добро пожаловать на канал</textarea>
    </div>

  </main>
</template>

<script>
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';
import ChannelView from './ChannelView.vue';

export default {
  components: {
    HeaderView,
    AsideView,
    ChannelView,
  },
};
</script>

<style>

</style>
