from colors import Colors
import pygame

class Block:
  def_init_(self, id):
    self.id = id
    self.cells = {}
    self.cell_size = 30
    self.rotation_state = 0
    self.colors = Colors.get_cell_colors()

  def draw(self, screen):
    tiles = self.cells[self.rotation_state]
    for tile in tiles:
      tiles_rect = pygame.Rect(title.column * self.cell_size + 1, title.row * self.cell_size + 1, self.cell_size -1, self.cell_size -1)
      pygame.draw.rect(screen, self.colors[self.id], title_rect)
