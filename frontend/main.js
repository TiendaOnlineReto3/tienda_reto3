
const app = Vue.createApp({
    data() {
        return {
            products:[],
            // products: [
            //     {
            //         id:1,
            //         nombre: 'Chaqueta corta',
            //         image: 'img/chaqueta1.avif',
            //         description: 'Chaqueta corta de hombre Lacoste acolchada e hidrófuga',
            //         price: 69.99,
            //         quantity: 1,
            //         category: 'Cazadora',
            //     },
            //     {
            //         id:2,
            //         nombre: 'Chaqueta de plumón',
            //         image: 'img/chaqueta2.avif',
            //         description: 'Packaway de tela con capucha y cremallera reversible',
            //         price: 49.99,
            //         quantity: 1,
            //         category: 'Cazadora',
            //     },
            //     {
            //         id:3,
            //         nombre: 'Chaqueta Sport',
            //         image: 'img/chaqueta3.avif',
            //         description: 'Fabricado con fibra reciclada con capucha y cremallera',
            //         price: 49.99,
            //         quantity: 1,
            //         category: 'Cazadora',
            //     },
            //     {
            //         id:4,
            //         nombre: 'Chaqueta bomber',
            //         image: 'img/chaqueta4.avif',
            //         description: 'Lacoste en tafetán acolchado con diseño reversible',
            //         price: 49.99,
            //         quantity: 1,
            //         category: 'Cazadora',
            //     },
            //     {
            //         id:5,
            //         nombre: 'Chaqueta acolchada',
            //         image: 'img/chaqueta5.avif',
            //         description: 'Lacoste en tafetán acolchado con diseño reversible',
            //         price: 49.99,
            //         quantity: 1,
            //         category: 'Cazadora',
            //     },
            //     {
            //         id: 6,
            //         nombre: 'Polo Clásico',
            //         image: 'img/camiseta1.avif',
            //         description: 'Polo clásico de Lacoste con un toque moderno y elegante',
            //         price: 59.99,
            //         quantity: 1,
            //         category: 'Camiseta',
            //     },
            //     {
            //         id: 7,
            //         nombre: 'Camiseta Polo Slim Fit',
            //         image: 'img/camiseta2.avif',
            //         description: 'Camiseta polo de Lacoste en ajuste Slim Fit para un estilo vanguardista',
            //         price: 69.99,
            //         quantity: 1,
            //         category: 'Camiseta',
            //     },
            //     {
            //         id: 8,
            //         nombre: 'Camiseta Casual Lacoste',
            //         image: 'img/camiseta3.avif',
            //         description: 'Camiseta casual Lacoste con detalles distintivos y comodidad excepcional',
            //         price: 79.99,
            //         quantity: 1,
            //         category: 'Camiseta',
            //     },
            //     {
            //         id: 9,
            //         nombre: 'Camiseta Elegante',
            //         image: 'img/camiseta4.avif',
            //         description: 'Camiseta elegante de Lacoste con diseño sofisticado y calidad premium',
            //         price: 89.99,
            //         quantity: 1,
            //         category: 'Camiseta',
            //     },
            //     {
            //         id: 10,
            //         nombre: 'Pantalón Deportivo',
            //         image: 'img/pantalon1.avif',
            //         description: 'Pantalón deportivo de Lacoste con estilo moderno y confort excepcional',
            //         price: 99.99,
            //         quantity: 1,
            //         category: 'Pantalon',
            //     },
            //     {
            //         id: 11,
            //         nombre: 'Pantalón Chino Slim Fit',
            //         image: 'img/pantalon2.avif',
            //         description: 'Pantalón chino de Lacoste en ajuste Slim Fit para un look casual y elegante',
            //         price: 109.99,
            //         quantity: 1,
            //         category: 'Pantalon',
            //     },
            //     {
            //         id: 12,
            //         nombre: 'Pantalón Jogger Lacoste',
            //         image: 'img/pantalon3.avif',
            //         description: 'Pantalón jogger de Lacoste para un estilo urbano y comodidad sin igual',
            //         price: 119.99,
            //         quantity: 1,
            //         category: 'Pantalon',
            //     },
            //     {
            //         id: 13,
            //         nombre: 'Pantalón Cargo Moderno',
            //         image: 'img/pantalon4.avif',
            //         description: 'Pantalón cargo de Lacoste con diseño moderno y múltiples bolsillos funcionales',
            //         price: 129.99,
            //         quantity: 1,
            //         category: 'Pantalon',
            //     },
            //     {
            //         id: 14,
            //         nombre: 'Pantalón Elegante',
            //         image: 'img/pantalon5.avif',
            //         description: 'Pantalón elegante de Lacoste con tejido premium y detalles refinados',
            //         price: 139.99,
            //         quantity: 1,
            //         category: 'Pantalon',
            //     },
            //     {
            //         id: 15,
            //         nombre: 'Sudadera Clásica Lacoste',
            //         image: 'img/sudadera1.avif',
            //         description: 'Sudadera clásica de Lacoste con logo icónico y comodidad inigualable',
            //         price: 149.99,
            //         quantity: 1,
            //         category: 'Sudadera',
            //     },
            //     {
            //         id: 16,
            //         nombre: 'Sudadera con Cierre',
            //         image: 'img/sudadera2.avif',
            //         description: 'Sudadera con cierre de Lacoste para un estilo versátil y moderno',
            //         price: 159.99,
            //         quantity: 1,
            //         category: 'Sudadera',
            //     },
            //     {
            //         id: 17,
            //         nombre: 'Sudadera Deportiva',
            //         image: 'img/sudadera3.avif',
            //         description: 'Sudadera deportiva de Lacoste con tecnología avanzada y diseño deportivo',
            //         price: 169.99,
            //         quantity: 1,
            //         category: 'Sudadera',
            //     },
            //     {
            //         id: 18,
            //         nombre: 'Sudadera Elegante',
            //         image: 'img/sudadera4.avif',
            //         description: 'Sudadera elegante de Lacoste con detalles refinados y estilo atemporal',
            //         price: 179.99,
            //         quantity: 1,
            //         category: 'Sudadera',
            //     },
            //     {
            //         id: 19,
            //         nombre: 'Sudadera con Capucha',
            //         image: 'img/sudadera5.avif',
            //         description: 'Sudadera con capucha de Lacoste para un look moderno y protección adicional',
            //         price: 189.99,
            //         quantity: 1,
            //         category: 'Sudadera',
            //     },
            //     {
            //         id: 20,
            //         nombre: 'Camiseta Suelta',
            //         image: 'img/chaqueta5.avif',
            //         description: 'Camiseta suelta de Lacoste con diseño reversible y estilo vanguardista',
            //         price: 199.99,
            //         quantity: 1,
            //         category: 'Camiseta',
            //     },
                
            
            isGridView: false,
            cart: [],
            isCartOpen: false,
            isUpdateIndicatorVisible: false,
            selectedCurrency: '', // Moneda por defecto
            selectedCategory: 'Todos', // Agrega esta línea
            favorites: [],
            isDragging: false,
            startX: 0,
            scrollLeft: 0,
            searchQuery: ''


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
        filteredProducts() {
            if (this.selectedCategory === 'Todos') {
                return this.products;
            } else {
                return this.products.filter(product => product.category === this.selectedCategory);
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
    },
    methods: {

        // Método para obtener datos de la API
        async fetchApiData() {
            try {
                const response = await fetch('http://64.226.73.41:5000/api/articulos');
                const data = await response.json();
                this.apiProducts = data;
            } catch (error) {
                console.error('Error al obtener datos de la API:', error);
            }
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
        // Método para actualizar la moneda seleccionada
        updateCurrency() {
            const apiKey = 'fca_live_1pwfsm4S40P2Q70dvJGfsmRYcwGF5eX0ukCk8cVG';
            const baseCurrency = 'USD';

            // Llamar a la API para obtener los tipos de cambio
            fetch(`https://freecurrencyapi.net/api/v2/latest?apikey=${apiKey}&base_currency=${baseCurrency}`)
                .then(response => response.json())
                .then(data => {
                    // Actualizar la moneda seleccionada
                    this.selectedCurrency = data.data.base_currency;

                    // Actualizar los precios de los productos según la moneda seleccionada
                    this.products.forEach(product => {
                        const originalPrice = product.price;
                        const exchangeRate = data.data.rates[this.selectedCurrency];
                        product.price = originalPrice * exchangeRate;
                    });
                })
                .catch(error => console.error('Error al obtener tipos de cambio:', error));
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
          isFavorite(index) {
            // Verifica si el producto está en la lista de favoritos
            return this.favorites.includes(this.filteredProducts[index]);
          }
    },
    watch: {
        // Observador para la moneda seleccionada
        selectedCurrency: 'updateCurrency',
    },
    mounted() {
        // Inicialmente, actualizar la moneda al cargar la página
        this.updateCurrency();
        document.addEventListener('mousemove', this.handleMouseMove);
        this.fetchApiData();

    },
    

});


app.mount('#app');