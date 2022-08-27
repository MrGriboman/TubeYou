<template>
  <aside class="min-h-screen hidden md:block xl:hidden overflow-auto fixed top-0 pt-12 bg-white z-20">
    <section>
      <ul>
        <li>
          <router-link to="/" class="flex flex-col items-center px-2 py-5 text-red-300 hover:bg-gray-100">
            <svg class="w-6 h-6 mb-1" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
            </svg>
            <span class="text-xs">Главная</span>
          </router-link>
          <router-link :to="`${this.channelLink}`" class="flex flex-col items-center px-2 py-5 text-red-300 hover:bg-gray-100">
            <svg class="w-6 h-6 mb-1 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"></path>
            </svg>
            <span class="text-xs">Мой канал</span>
          </router-link>
          <router-link :to="`${this.studioLink}`" class="flex flex-col items-center px-2 py-5 text-red-300 hover:bg-gray-100">
            <svg class="w-6 h-6 mb-1 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z"></path>
            </svg>
            <span class="text-xs">Творческая студия</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
  <aside class="hidden xl:block w-64 min-h-screen overflow-auto fixed top-0 pt-12 bg-white z-20">
    <section class="py-2 border-b">
      <ul>
        <li>
          <router-link to="/" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
            <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
            </svg>
            <span>Главная</span>
          </router-link>
          <router-link :to="`${this.channelLink}`" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
            <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"></path>
            </svg>
            <span>Мой канал</span>
          </router-link>
        </li>
      </ul>
    </section>
    <section class="py-2 border-b">
      <ul>
        <li>
          <router-link :to="`${this.studioLink}`" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
            <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                 xmlns="http://www.w3.org/2000/svg">
              <path
                d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z"></path>
            </svg>
            <span>Творческая студия</span>
          </router-link>
        </li>
      </ul>
    </section>
  </aside>
  <div class=" hidden fixed inset-0 bg-black bg-opacity-50 z-30">
    <aside class="w-64 min-h-screen overflow-auto bg-white">
      <section class="flex items-center p-4 border-b sticky top-0 bg-white">
        <button class="ml-2 mr-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
               stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h8m-8 6h16"/>
          </svg>
        </button>
        <a href=" ">
          <svg width="50px" height="50px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="linear-gradient" x1="0.5" x2="0.5" y2="1" gradientUnits="objectBoundingBox">
                <stop offset="0" stop-color="#ff0069"/>
                <stop offset="1" stop-color="#b3002b"/>
              </linearGradient>
              <clipPath id="clip-Video">
                <rect width="48" height="48"/>
              </clipPath>
            </defs>
            <g id="Video" clip-path="url(#clip-Video)">
              <rect width="48" height="48" fill="rgba(255,255,255,0)"/>
              <g id="Video-2" data-name="Video" transform="translate(4 12)">
                <g id="Icon" transform="translate(26)" stroke-miterlimit="10" fill="url(#linear-gradient)">
                  <path
                    d="M0,13.6a2,2,0,0,0,.891,1.665l10,6.661A2,2,0,0,0,14,20.265V3.735a2,2,0,0,0-3.109-1.665l-10,6.661A2,2,0,0,0,0,10.4Z"
                    stroke="none"/>
                  <path
                    d="M 11.99444007873535 22.26802062988281 L 11.99442005157471 21.76802062988281 L 11.99450016021729 21.76802062988281 C 12.71852970123291 21.76802062988281 13.5 21.19325065612793 13.5 20.2646598815918 L 13.5 3.735340118408203 C 13.5 2.806750059127808 12.71842956542969 2.231980085372925 11.99431037902832 2.231980085372925 C 11.70028018951416 2.231980085372925 11.4224100112915 2.317759990692139 11.16841983795166 2.486949920654297 L 1.16841995716095 9.14818000793457 C 0.7498800158500671 9.426980018615723 0.5 9.893670082092285 0.5 10.39657020568848 L 0.5 13.60342979431152 C 0.5 14.10632991790771 0.7498800158500671 14.57301998138428 1.16841995716095 14.85181999206543 L 11.16841983795166 21.5130500793457 C 11.41880035400391 21.67983055114746 11.70440006256104 21.76799964904785 11.99435997009277 21.76802062988281 L 11.99444007873535 22.26802062988281 M 11.9943151473999 22.26802062988281 C 11.62259006500244 22.26798629760742 11.2412052154541 22.16230583190918 10.8912296295166 21.92918014526367 L 0.8912299871444702 15.2679500579834 C 0.3344700038433075 14.89708042144775 -8.881784197001252e-16 14.27241039276123 -8.881784197001252e-16 13.60342979431152 L -8.881784197001252e-16 10.39657020568848 C -8.881784197001252e-16 9.72758960723877 0.3344700038433075 9.102919578552246 0.8912299871444702 8.732049942016602 L 10.8912296295166 2.070820093154907 C 11.241286277771 1.837640404701233 11.62250804901123 1.731979131698608 11.9943151473999 1.731979131698608 C 13.03425407409668 1.731979131698608 14 2.558899879455566 14 3.735340118408203 L 14 20.2646598815918 C 14 21.44119834899902 13.03435230255127 22.26811599731445 11.9943151473999 22.26802062988281 Z"
                    stroke="none" fill="rgba(255,255,255,0.3)"/>
                </g>
                <g id="Icon-2" data-name="Icon" fill="rgba(255,125,148,0.6)" stroke="rgba(255,255,255,0.3)"
                   stroke-miterlimit="10" stroke-width="0.5">
                  <rect width="32" height="24" rx="2" stroke="none"/>
                  <rect x="0.25" y="0.25" width="31.5" height="23.5" rx="1.75" fill="none"/>
                </g>
                <path id="Icon-3" data-name="Icon"
                      d="M7,2.5A2.5,2.5,0,1,1,9.5,5,2.5,2.5,0,0,1,7,2.5Zm-7,0A2.5,2.5,0,1,1,2.5,5,2.5,2.5,0,0,1,0,2.5Z"
                      transform="translate(4 4)" fill="#fff"/>
              </g>
            </g>
          </svg>

        </a>
      </section>
      <section class="py-2 border-b">
        <ul>
          <li>
            <router-link to="/" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
              <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M10.707 2.293a1 1 0 00-1.414 0l-7 7a1 1 0 001.414 1.414L4 10.414V17a1 1 0 001 1h2a1 1 0 001-1v-2a1 1 0 011-1h2a1 1 0 011 1v2a1 1 0 001 1h2a1 1 0 001-1v-6.586l.293.293a1 1 0 001.414-1.414l-7-7z"></path>
              </svg>
              <span>Главная</span>
            </router-link>
            <router-link :to="`${this.channelLink}`" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
              <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M9 6a3 3 0 11-6 0 3 3 0 016 0zM17 6a3 3 0 11-6 0 3 3 0 016 0zM12.93 17c.046-.327.07-.66.07-1a6.97 6.97 0 00-1.5-4.33A5 5 0 0119 16v1h-6.07zM6 11a5 5 0 015 5v1H1v-1a5 5 0 015-5z"></path>
              </svg>
              <span>Мой канал</span>
            </router-link>
          </li>
        </ul>
      </section>
      <section class="py-2 border-b">
        <ul>
          <li>
            <router-link :to="`${this.studioLink}`" class="flex items-center px-6 py-2 text-sm hover:bg-gray-100">
              <svg class="w-6 h-6 mr-4 text-red-200" fill="currentColor" viewBox="0 0 20 20"
                   xmlns="http://www.w3.org/2000/svg">
                <path
                  d="M2 5a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2V5zm14 1a1 1 0 11-2 0 1 1 0 012 0zM2 13a2 2 0 012-2h12a2 2 0 012 2v2a2 2 0 01-2 2H4a2 2 0 01-2-2v-2zm14 1a1 1 0 11-2 0 1 1 0 012 0z"></path>
              </svg>
              <span>Творческая студия</span>
            </router-link>
          </li>
        </ul>
      </section>

    </aside>
  </div>

</template>

<script>
export default {
  data() {
    return {
      authorized: false,
      channelLink: '/channel/:id',
      studioLink: '/studio',
    }
  },

  async mounted() {
    this.authorized = localStorage.getItem('authToken') ? true : false
    if (!this.authorized) {
      this.channelLink = '/login'
      this.studioLink = '/login'
    } 
  }
};
</script>

<style>
 .router-link-active svg{
     @apply text-red-500;
 }
</style>
