<template>
  <v-footer
    dark
    padless
  >
    <v-card
      width="100%"
      flat
      tile
      class="indigo lighten-1 white--text text-center"
    >
      <v-card-text>
        <v-btn @click="RedirectTo(icon.to)"
          v-for="icon in icons"
          :key="icon.icon"
          class="mx-4 white--text"
          icon
        >
          <v-icon size="24px">
            {{ icon.icon }}
          </v-icon>
        </v-btn>
      </v-card-text>

      <v-card-text class="white--text pt-0">
          BomDji
      </v-card-text>

      <v-divider></v-divider>

      <v-card-text class="white--text">
        {{ new Date().getFullYear() }} — <strong>Київ</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>

<script>
  export default {
    data: () => ({
      icons: [
        { icon: 'mdi-github', to: 'https://github.com/BomDji/Int20h-Test-Exercise'}
      ],
    }),
    methods: { 
        RedirectTo(to) {
                location.href = to;
            }
        }
  }
</script>