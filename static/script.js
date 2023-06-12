(function() {
    const content = document.getElementsByClassName('folium-map')
    if (content.length !== 0) {
        const foliumMap = content[0];
        foliumMap.addEventListener('click', (event) => {
            console.log(event, 'clicked');
        })
    }
})();