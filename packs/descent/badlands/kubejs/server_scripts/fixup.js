// priority: 0

// Visit the wiki for more info - https://kubejs.com/

ServerEvents.tags('item', event => {
  event.add('forge:sandstone/venus_sandstone', 'ad_astra:venus_sandstone')
})

ServerEvents.tags('worldgen/biome', event => {
  event.removeAll("immersive_weathering:has_lakebed")
})
