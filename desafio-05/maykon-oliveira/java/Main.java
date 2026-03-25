import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import models.*;

/**
 *
 * @author Maykon Oliveira
 */
public class Main {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) throws FileNotFoundException {
        List<Funcionario> funcionariosList = new ArrayList<>();
        List<Area> areasList = new ArrayList<>();
        FileReader JSON_FILE;

        if (args.length > 0) {
            JSON_FILE = new FileReader(args[0]);
        } else {
            JSON_FILE = new FileReader("..\\funcionarios.json");
        }

        Gson gson = new Gson();
        JsonParser parser = new JsonParser();
        JsonElement jsonElement = parser.parse(JSON_FILE);

        if (jsonElement.isJsonObject()) {
            JsonObject jsonObject = jsonElement.getAsJsonObject();
            JsonArray funcionarioArrayJson = jsonObject.getAsJsonArray("funcionarios");
            JsonArray areaArrayJson = jsonObject.getAsJsonArray("areas");

            for (JsonElement funcionario : funcionarioArrayJson) {
                funcionariosList.add(gson.fromJson(funcionario, Funcionario.class));
            }

            for (JsonElement area : areaArrayJson) {
                areasList.add(gson.fromJson(area, Area.class));
            }
        }
        Manager manager = new Manager(funcionariosList, areasList);
        manager.salariosGlobais();
        manager.salariosPorArea();
        manager.numeroFuncionarioPorArea();
        manager.salariosMesmoSobrenome();
    }

}
