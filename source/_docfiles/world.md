# World

This chapter covers the world view.

## Entities

### Coral the robot

Coral executes the commands of the program.

### Slab

// TODO: formatting
| | |
| --------------------- | --- |
| Placeable by program | ✅ |
| Placeable in viewport | ✅ |

### Cube

Cannot be placed by Coral during runtime. Coral is not able to step on a cube.

### Flag

Coral can place flags underneath himself.

## View

The world view is a 3d canvas featuring Coral the robot on a grid structure.

## Camera

The camera can be controlled using the mouse and multi-touch. It supports zoom, rotation and translation.

| Camera Action     | Mouse                   | Touch            |
| ----------------- | ----------------------- | ---------------- |
| Rotate vieport    | Hold left mouse button  | One finger drag  |
| Translate vieport | Hold right mouse button | Two finger drag  |
| Zoom              | Scroll wheel            | Two finger pinch |

## UI

### Reset Camera

Reset the camera view position and angle.

### Inventory

Only displayed when inventory is enabled. Displays the current amount of slabs in the inventory.

### Step

Move Coral one step forward if possible.

### Rotate counterclockwise

Rotate Coral to the left.

### Rotate clockwise

Rotate Coral to the right.

### Change placement mode

Change the type of object to place in the world.

### Change color

Change the color of the items to place.

### Put down

Put down an entity.

### Pick up

Pick up an entity.

### Expand/Collapse settings

Expand/Collapse additional settings.

### Additional settings

#### Reset world

Reset the world to the default.

#### Resize world

Opens a modal to adjust world size.

#### Save world as default

Save the current world state as the default.

#### Import world

See Titlebar -> World -> Import World

#### Export world

See Titlebar -> World -> Export World
