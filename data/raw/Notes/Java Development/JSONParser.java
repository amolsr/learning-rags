import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.List;
import java.util.Map;
 
import javax.script.ScriptEngine;
import javax.script.ScriptEngineManager;
import javax.script.ScriptException;
 
public class JSONParser {
 
    public void parse(String json) throws ScriptException {
        ScriptEngineManager sem = new ScriptEngineManager();
        scriptEngine = sem.getEngineByName("javascript");
        String script = "Java.asJSONCompatible(" + json + ")";
        Object result = scriptEngine.eval(script);
        Map contents = (Map) result;
         
        contents.forEach((k,v) ->{
            System.out.println("Key => "+k +" value =>"+contents.get(k));
        });
         
        List data = (List) contents.get("data");
        data.forEach(d ->{
            Map matchDetail = (Map) d;
            matchDetail.forEach((k,v) ->{
                System.out.println("Key => "+k +" value =>"+matchDetail.get(k));
            }); 
        });
    }
 
}
