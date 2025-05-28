<script>
import { ref, watch, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import axios from 'axios'

const route = useRoute()
const productos = ref([])

async function fetchProducts() {
  let url = '/api/products/'
  const search = route.query.search
  if (search) {
    url += `?search=${encodeURIComponent(search)}`
  }

  const token = localStorage.getItem('access')
  const headers = token ? { Authorization: `Bearer ${token}` } : {}

  const response = await axios.get(url, { headers })
  productos.value = response.data.results || response.data
}

onMounted(fetchProducts)

watch(() => route.query.search, fetchProducts)
</script>