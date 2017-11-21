package memius.com.memius40;

import android.os.AsyncTask;
import android.widget.EditText;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import org.json.*;

import java.util.concurrent.ExecutionException;

/**
 * Created by lexay on 18.11.2017.
 */

class RegistrationTask extends AsyncTask<String, Void, JSONObject> {
    private  OnTaskCompleted listener;
//    private Exception exception;
    EditText login;
    EditText password;
    public RegistrationTask ( OnTaskCompleted listener,EditText l, EditText r){
        this.listener = listener;
        login = l;
        password = r;
    }


    protected JSONObject doInBackground(String... urls) {

        try {

            String url = GlobalVars.url + "Registration.py";
            HttpResponse<String> response = Unirest.post(url)
                    .header("content-type", "application/x-www-form-urlencoded")
                    .body("Username=" + login.getText().toString() + "&Password=" + password.getText().toString())
                    .asString();


            JSONObject responseBody = new JSONObject(response.getBody().toString());

            return responseBody;
        }
        catch(Exception e) {
            System.out.println("Error: " + e.toString());
            return null;
        }
    }

    protected void onPostExecute(JSONObject feed) {
        try {
            listener.onTaskCompleted();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}