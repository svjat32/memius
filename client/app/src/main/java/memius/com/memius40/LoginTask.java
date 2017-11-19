package memius.com.memius40;

import android.os.AsyncTask;
import android.widget.EditText;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;

import org.json.JSONObject;

import java.util.concurrent.ExecutionException;

import android.os.AsyncTask;
import android.widget.EditText;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import org.json.*;

import java.util.concurrent.ExecutionException;

/**
 * Created by lexay on 18.11.2017.
 */

class LoginTask extends AsyncTask<String, Void, JSONObject> {
    private  OnTaskCompleted listener;
    //    private Exception exception;
    EditText login;
    EditText password;
    public LoginTask ( OnTaskCompleted listener, EditText l,EditText r){
        this.listener = listener;
        login = l;
        password = r;
    }


    protected JSONObject doInBackground(String... urls) {

        try {

            String url = "http://91.225.131.175:8000/cgi-bin/Registration.py";
            HttpResponse<String> jsonResponse = Unirest.post(url)
                    .header("content-type", "application/x-www-form-urlencoded")
                    .body("Username=" + login.getText() + "&Password=" + password.getText()+"&RememberMe=true")
                    .asString();


            JSONObject responseBody = new JSONObject(jsonResponse.getBody().toString());

            return responseBody;
        }
        catch(Exception e) {
            System.out.println("Error: " + e.toString());
            return null;
        }
    }

    protected void onPostExecute(JSONObject feed) {
        try {
            listener.onTaskComleted();
        } catch (ExecutionException e) {
            e.printStackTrace();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
}