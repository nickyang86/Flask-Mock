<template>
  <div />
</template>

<script>
import { test } from '@/api/general'
export default {
  name: 'Index',
  data() {
    return {
      info: ''
    }
  },
  created() {
    this.getInfo()
  },
  methods: {
    getInfo: function() {
      test()
    }
  }
}
</script>

<style scoped>

</style>
