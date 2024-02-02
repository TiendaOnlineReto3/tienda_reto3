new Vue({
  el: '#app',
  data: {
    cards: [],
    isGridView: false,
    scrollLeft: 0,
    isUpdateIndicatorVisible: false,
    startX: 0,
    isDragging: false,
    searchQuery: '',
    selectedCategory: 'Todos', // Agrega esta línea


  },
  mounted() {
    this.fetchData();
  },
  
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://52.90.222.243/api/product');
        const data = await response.json();
        this.cards = data;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
    increaseQuantity(card) {
      card.quantity++;
    },
    decreaseQuantity(card) {
      if (card.quantity > 1) {
        card.quantity--;
      }
    },
    handleMouseDown(event) {
      this.isDragging = true;
      this.startX = event.pageX - this.$refs.cardRow.offsetLeft;
      this.scrollLeft = this.$refs.cardRow.scrollLeft;
    },
    handleMouseUp() {
      this.isDragging = false;
    },
    handleMouseMove(event) {
      if (!this.isDragging) return;
      const x = event.pageX - this.$refs.cardRow.offsetLeft;
      const walk = (x - this.startX) * 3; // Ajusta este valor según tus preferencias
      this.$refs.cardRow.scrollLeft = this.scrollLeft - walk;
    },
    toggleView() {
      this.isGridView = !this.isGridView;
    },
    setGridView() {
      this.isGridView = true;
    },
    setRowView() {
      this.isGridView = false;
    },
 
  },
});
