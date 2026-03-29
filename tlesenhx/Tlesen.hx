package tlesenhx;

@:pythonImport("tlesenpy.tlesen", "Taibolesen")
extern class Taibolesen {
    public var screen:Dynamic;
    public var width:Int;
    public var height:Int;
    public function new(width:Int, height:Int);
    public function clear_layered():Void;
    public function clear(r:Int, g:Int, b:Int):Void;
    public function load_image(path:String):Dynamic;
    public function draw_image(image:Dynamic, x:Float, y:Float):Void;
    public function get_keys():Dynamic;
    public function run(updateCallback:Void -> Void):Void;
}

@:pythonImport("pygame")
extern class KeyCodes {
    @:native("K_LEFT") static var LEFT:Int;
    @:native("K_RIGHT") static var RIGHT:Int;
    @:native("K_SPACE") static var SPACE:Int;
}

@:pythonImport("pygame.draw")
extern class Draw {
    @:native("rect")
    public static function rect(surface:Dynamic, color:Array<Int>, rect:Array<Int>, width:Int = 0):Void;
}

// The main class of this file
class Tlesen {
    public static function init(w:Int, h:Int):Taibolesen {
        return new Taibolesen(w, h);
    }
}