package memius.com.memius40;

import android.os.AsyncTask;

import com.mashape.unirest.http.HttpResponse;
import com.mashape.unirest.http.Unirest;
import org.json.*;

/**
 * Created by lexay on 18.11.2017.
 */

class RegistrationTask extends AsyncTask<String, Void, String> {

    private Exception exception;

    protected JSONObject doInBackground(String... urls) {
        try {
            String url = "http://91.225.131.175:8000/cgi-bin/reg.py";
            HttpResponse<String> jsonResponse = Unirest.post(url)
                    .header("content-type", "application/x-www-form-urlencoded")
                    .body("Username=" + "user" + "&Password=" + "pass" + "&E-mail=" + "email")
                    .asString();


            JSONObject responseBody = new JSONObject(jsonResponse.getBody().toString());
            //String status = responseBody.getString("Status");


            return responseBody;
        }
        catch(Exception e) {
            System.out.println("Error: " + e.toString());
            return null;
        }
    }

    protected void onPostExecute(String feed) {
        // TODO: check this.exception
        // TODO: do something with the feed
    }
}