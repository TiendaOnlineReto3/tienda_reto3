
const app = Vue.createApp({
    data() {
        return {
            products: [],
            isGridView: false,
            cart: [],
            isCartOpen: false,
            isUpdateIndicatorVisible: false,
            selectedCategory: 'Todos', // Cambiar de currentCategory a selectedCategory
            favorites: [],
            isDragging: false,
            startX: 0,
            scrollLeft: 0,
            searchQuery: '',
            showFirstIcon: true,
        };

        
    },
    computed: {
        filteredCamisetas() {
            return this.products.filter(product => product.category === 'Camiseta');
        },
        filteredCazadoras() {
            return this.products.filter(product => product.category === 'Cazadora');
        },
        filteredPantalones() {
            return this.products.filter(product => product.category === 'Pantalon');
        },
        filteredSudaderas() {
            return this.products.filter(product => product.category === 'Sudadera');
        },
        /*
        filteredProducts() {
            if (this.currentCategory === 'Todos') {
                return this.products;
            } else {
                return this.products.filter(product => product.category === this.currentCategory);
            }
        },
        filteredProducts() {
            if (this.selectedCategory === 'Todos') {
              return this.products.filter(product =>
                product.nombre.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                product.description.toLowerCase().includes(this.searchQuery.toLowerCase())
              );
            } else {
              return this.products.filter(product =>
                (product.category === this.selectedCategory) &&
                (product.nombre.toLowerCase().includes(this.searchQuery.toLowerCase()) ||
                  product.description.toLowerCase().includes(this.searchQuery.toLowerCase()))
              );
            }
          },
          */
         filteredProducts(){
          return this.products
         }
    },
    methods: {
        obtenerProductos() {
    fetch('http://54.221.123.46/api/product')
      .then(response => {
        if (!response.ok) {
          throw new Error(`HTTP error! Status: ${response.status}`);
        }
        return response.json();
      })
      .then(data => {
        this.products = data;
        console.log("Productos de la API: " , this.products)
      })
      .catch(error => {
        console.error('Error al obtener datos:', error);
      });
  },

        addToFavorites(index) {
            // Tu lógica para añadir o quitar de favoritos aquí
            // Por ejemplo, podrías invertir el valor de showFirstIcon
            this.showFirstIcon = !this.showFirstIcon;
          },
          isFavorite(index) {
            // Implementa tu lógica para verificar si está en favoritos
            // Retorna true o false según sea necesario
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
        selectCategory(category) {
            this.selectedCategory = category;
        },
        decreaseQuantity(product) {
            if (product.quantity > 1) {
              product.quantity--;
            }
          },
          // Método para aumentar la cantidad
          increaseQuantity(product) {
            product.quantity++;
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
        addToCart(index, quantity) {
            const existingCartItemIndex = this.cart.findIndex(item => item.index === index);

            if (existingCartItemIndex !== -1) {
                // Si el producto ya está en el carrito, actualiza la cantidad
                this.cart[existingCartItemIndex].quantity += quantity;
            } else {
                // Si el producto no está en el carrito, agrégalo
                this.cart.push({ index, quantity });
            }

            // Mostrar el indicador de actualización
            this.isUpdateIndicatorVisible = true;
        },
        removeFromCart(index) {
            this.cart.splice(index, 1);
        },
        calculateTotal() {
            return this.cart.reduce((total, item) => total + this.products[item.index].price * item.quantity, 0);
        },
        toggleCart() {
            this.isCartOpen = !this.isCartOpen;
        },
        countTotalItemsInCart() {
            return this.cart.reduce((totalItems, item) => totalItems + item.quantity, 0);
        },
        formatPrice(price) {
            return `$${price.toFixed(2)}`;
        },
        filterByCategory(category) {
            this.selectedCategory = category;
        },
        addToFavorites(index) {
            // Agrega el producto al array de favoritos
            this.favorites.push(this.filteredProducts[index]);
          },
          removeFromFavorites(index) {
            // Remueve el producto del array de favoritos
            this.favorites.splice(index, 1);
          },

          toggleFavorite(index) {
            this.iconChanged = !this.iconChanged;
            // Lógica para agregar o quitar de favoritos...
          },
    },
    watch: {
        
    },
    mounted() {
        this.obtenerProductos()
        // Inicialmente, actualizar la moneda al cargar la página
        document.addEventListener('mousemove', this.handleMouseMove);

    },
    

});


app.mount('#app');