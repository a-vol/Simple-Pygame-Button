class Button:

  def __init__(self, surface, dColour, lColour, rect, text=''):
    self.surface = surface
    self.Rect = rect
    self.rect = pygame.Rect(rect)
    self.dColour = dColour
    self.lColour = lColour
    self.text = text

  def checkClick(self, events):
    for event in events:
      if event.type == pygame.MOUSEBUTTONDOWN:
        if self.rect.collidepoint(event.pos):
          return True

  def checkHover(self, rect, events):
    for event in events:
      if event.type == pygame.MOUSEMOTION:
        hovered = (rect).collidepoint(event.pos)
        return hovered

  def drawRect(self, events):
    for event in events:
      if self.checkHover(self.rect, events):
        pygame.draw.rect(screen, self.lColour, (self.rect))
      else:
        pygame.draw.rect(screen, self.dColour, (self.rect))

    rect = self.rect
    text_surface = font.render(self.text, False, font_color)
    text_rect = text_surface.get_rect()
    text_rect.center = (rect[2] // 2) + rect[0], (rect[3] // 2) + rect[1]

    screen.blit(text_surface, text_rect)
