import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;

public class CRUD {

  private static Connection con;
  
	private DBcrud() {
		// TODO Auto-generated constructor stub
      try {
			  this.con = DriverManager.getConnection(System.getenv("DATABASE_HOST"), System.getenv("DBUSER"), System.getenv("DBPASS"));
		  } catch (Exception e) {
			  System.out.println(e);
		  }
	};

	public int create(String user, String pass) {
		int i = 0;
    Connection con = con;
		String sql = "INSERT INTO table (User, Password) VALUES(?, ?) ";
		PreparedStatement ps = con.prepareStatement(sql);
		ps.setString(1, user);
		ps.setString(2, pass);
		i = ps.executeUpdate();
		if (i > 0) {
			System.out.println("A new user was inserted successfully!");
		}
		return i;
	}

	public String read(String user, String pass) {
		Connection con = con;
		PreparedStatement ps = con.prepareStatement("SELECT * FROM table WHERE User = BINARY ? AND Password = BINARY ?");
		ps.setString(1, user);
		ps.setString(2, pass);
		ResultSet rs = ps.executeQuery();
		if (rs.next()) {
			return rs.getString("User");
		}
		return null;
	}

	public void Update(String user, String pass) {
		Connection con = con;
		String sql = "UPDATE Admin SET Password = ? WHERE User = BINARY ?;";
		PreparedStatement statement = con.prepareStatement(sql);
		statement.setString(1, pass);
		statement.setString(2, user);
		int rowsUpdated = statement.executeUpdate();
		if (rowsUpdated > 0) {
			System.out.println("An existing user was updated successfully!");
		}
	}
}
