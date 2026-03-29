# Taibolesen Game Framework

Taibolesen is a game framework designed for developers to make simple games
in Haxe

example

```
import tlesenhx.Tlesen;

// Raindrop class defined here so it's globally available to Main
class Raindrop {
    public var x:Float;
    public var y:Float;
    public var speed:Float;
    public var length:Int;
    
    public function new(screenW:Int, screenH:Int) {
        respawn(screenW, screenH);
        this.y = Math.random() * screenH; 
    }

    public function respawn(screenW:Int, screenH:Int) {
        this.x = Math.random() * screenW;
        this.y = -20;
        this.speed = 10 + Math.random() * 10;
        this.length = 5 + Std.int(Math.random() * 15);
    }

    public function update(screenW:Int, screenH:Int) {
        this.y += this.speed;
        if (this.y > screenH) respawn(screenW, screenH);
    }
}

class Main {
    static function main() {
        // Initialize the engine
        var engine = tlesenhx.Tlesen.init(800, 600);
        var playerImg = engine.load_image("dude.png");
        
        var px:Float = 100;
        var py:Float = 400;

        // CRITICAL: Explicitly type the array so Haxe can iterate on it
        var raindrops:Array<Raindrop> = [];
        for (i in 0...150) {
            raindrops.push(new Raindrop(800, 600));
        }

        function update() {
            var keys = engine.get_keys();
            
            // Movement - Accessing KeyCodes through the Tlesen module
            if (python.Syntax.code("{0}[{1}]", keys, tlesenhx.Tlesen.KeyCodes.LEFT)) px -= 7;
            if (python.Syntax.code("{0}[{1}]", keys, tlesenhx.Tlesen.KeyCodes.RIGHT)) px += 7;

            // Update Rain
            for (drop in raindrops) {
                drop.update(engine.width, engine.height);
            }

            // Keep player on floor
            if (py > engine.height - 100) py = engine.height - 100;

            // Rendering
            engine.clear_layered();
            engine.draw_image(playerImg, px, py);
            
            for (drop in raindrops) {
                tlesenhx.Tlesen.Draw.rect(
                    engine.screen, 
                    [180, 180, 200], 
                    [Std.int(drop.x), Std.int(drop.y), 2, drop.length]
                );
            }
        }

        engine.run(update);
    }
}
```

# Contributing

you can make the engine better by doing the Fork-and-Pull Method

# Requirements

Haxe (https://haxe.org)

Python (https://python.org)

Pygame (https://pygame.org)









      
